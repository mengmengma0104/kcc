# -*- coding: utf-8 -*-
"""Capture the running app window and quality-check the result.

Launches the built exe via the shell, locates its Qt window, captures it with
PrintWindow (so DirectComposition content renders), then verifies the capture
numerically — a dark background and a healthy amount of near-white text pixels
mean the UI painted correctly. Written as a sanity gate because Qt does not
always repaint freshly exposed regions after a window resize.

Output: docs/screenshot.png (usable inline in README).
"""
import ctypes
import os
import sys
import time
from ctypes import wintypes

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EXE_NAME = 'KCC_11.2.0_zh.exe'
EXE = os.path.join(ROOT, 'dist', EXE_NAME)
OUT = os.path.join(ROOT, 'docs', 'screenshot.png')

user32 = ctypes.WinDLL('user32', use_last_error=True)
gdi32 = ctypes.WinDLL('gdi32', use_last_error=True)
kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)

MIN_COLORS = 100        # a painted UI has a rich palette
MIN_TEXT_PIXELS = 1500  # near-white pixel samples, i.e. rendered text
MAX_BG_BRIGHTNESS = 80  # the app uses a dark theme
PROCESS_TERMINATE = 0x0001


def find_window(timeout=90):
    """Return (hwnd, pid) of the app's visible Qt window, or (None, None)."""
    deadline = time.time() + timeout
    while time.time() < deadline:
        time.sleep(2)
        hits = []
        proc = ctypes.WINFUNCTYPE(ctypes.c_bool, ctypes.c_void_p, ctypes.c_void_p)

        def cb(h, _l):
            cls = ctypes.create_unicode_buffer(256)
            user32.GetClassNameW(h, cls, 256)
            if user32.IsWindowVisible(h) and 'QWindow' in cls.value:
                n = user32.GetWindowTextLengthW(h)
                buf = ctypes.create_unicode_buffer(n + 1)
                user32.GetWindowTextW(h, buf, n + 1)
                if EXE_NAME in buf.value or '漫画' in buf.value:
                    pid = ctypes.c_ulong()
                    user32.GetWindowThreadProcessId(h, ctypes.byref(pid))
                    hits.append((h, pid.value))
            return True

        user32.EnumWindows(proc(cb), 0)
        if hits:
            return hits[0]
    return None, None


def terminate(pid):
    """Terminate the GUI process by pid (the app minimizes to tray on WM_CLOSE)."""
    handle = kernel32.OpenProcess(PROCESS_TERMINATE, False, pid)
    if not handle:
        return False
    try:
        kernel32.TerminateProcess(handle, 0)
    finally:
        kernel32.CloseHandle(handle)
    return True


def capture(hwnd):
    """PrintWindow capture of the given window; returns a PIL image."""
    rect = wintypes.RECT()
    user32.GetWindowRect(hwnd, ctypes.byref(rect))
    w, h = rect.right - rect.left, rect.bottom - rect.top

    hdc = user32.GetWindowDC(hwnd)
    mdc = gdi32.CreateCompatibleDC(hdc)
    bmp = gdi32.CreateCompatibleBitmap(hdc, w, h)
    try:
        gdi32.SelectObject(mdc, bmp)
        user32.PrintWindow(hwnd, mdc, 2)   # PW_RENDERFULLCONTENT

        class BMIH(ctypes.Structure):
            _fields_ = [('biSize', wintypes.DWORD), ('biWidth', wintypes.LONG),
                        ('biHeight', wintypes.LONG), ('biPlanes', wintypes.WORD),
                        ('biBitCount', wintypes.WORD), ('biCompression', wintypes.DWORD),
                        ('biSizeImage', wintypes.DWORD), ('biXPelsPerMeter', wintypes.LONG),
                        ('biYPelsPerMeter', wintypes.LONG), ('biClrUsed', wintypes.DWORD),
                        ('biClrImportant', wintypes.DWORD)]

        bmi = BMIH()
        bmi.biSize = ctypes.sizeof(BMIH)
        bmi.biWidth, bmi.biHeight, bmi.biPlanes = w, -h, 1
        bmi.biBitCount, bmi.biCompression = 32, 0
        buf = ctypes.create_string_buffer(w * h * 4)
        gdi32.GetDIBits(mdc, bmp, 0, h, buf, ctypes.byref(bmi), 0)
    finally:
        gdi32.DeleteObject(bmp)
        gdi32.DeleteDC(mdc)
        user32.ReleaseDC(hwnd, hdc)

    from PIL import Image
    return Image.frombuffer('RGBA', (w, h), buf.raw, 'raw', 'BGRA', 0, 1).convert('RGB')


def quality(img):
    """Return (ok, stats) describing whether the capture looks like a painted UI."""
    colors = {}
    px = img.load()
    w, h = img.size
    for y in range(0, h, 3):
        for x in range(0, w, 3):
            colors[px[x, y]] = colors.get(px[x, y], 0) + 1
    bg = max(colors.items(), key=lambda kv: kv[1])[0]
    text_px = sum(v for (r, g, b), v in colors.items() if r > 200 and g > 200 and b > 200)
    ok = (bg[0] <= MAX_BG_BRIGHTNESS and len(colors) >= MIN_COLORS
          and text_px >= MIN_TEXT_PIXELS)
    return ok, {'size': img.size, 'bg': bg, 'colors': len(colors), 'text_pixels': text_px}


def main():
    if not os.path.exists(EXE):
        raise SystemExit('build the exe first: %s not found' % EXE)

    os.startfile(EXE)                     # 由 shell 启动，无需 subprocess
    print('launched %s, waiting for its window...' % EXE_NAME)
    hwnd, pid = find_window()
    if not hwnd:
        raise SystemExit('window not found within timeout')
    print('window:', hex(hwnd), 'pid:', pid)

    ok = False
    try:
        user32.SetForegroundWindow(hwnd)
        time.sleep(1.5)
        img = capture(hwnd)
        ok, stats = quality(img)
        print('capture stats:', stats)

        if ok or not os.path.exists(OUT):
            # 仅在质检通过（或尚无既有截图）时写入，避免用未重绘的画面覆盖好图
            os.makedirs(os.path.dirname(OUT), exist_ok=True)
            img.save(OUT)
            print('saved:', OUT, '| quality_ok:', ok)
        else:
            print('keeping existing %s (新画面未通过质检，未覆盖)' % OUT)
    finally:
        terminate(pid)

    if not ok:
        print('WARNING: capture looks unpainted (dark theme + text pixels expected). '
              'Resize the window manually before capturing, or retry — Qt may not '
              'repaint freshly exposed regions right after launch.')
        return 1
    return 0


if __name__ == '__main__':
    sys.exit(main())
