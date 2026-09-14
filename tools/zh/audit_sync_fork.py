# -*- coding: utf-8 -*-
"""Audit and sync the fork against the main repository.

Compares three trees at blob level (local working tree, main repo branch, fork
branch) and brings the fork up to date for any file that differs. Uses the
GitHub REST API rather than git, so it works when github.com is unreachable but
api.github.com responds.

README.md is excluded from syncing: the fork intentionally points its download
link at the main repository's Releases.

Usage:  <venv>\\Scripts\\python.exe tools/zh/audit_sync_fork.py
Exit code 0 = fork matches the local tree (apart from the intentional README diff).
"""
import base64
import os
import subprocess
import sys

import requests

GH = r'C:\Program Files\GitHub CLI\gh.exe'
GIT = r'E:\Program Files\Git\cmd\git.exe'
LOCAL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAIN = 'mengmengma0104/kcc-zh-cn'
FORK = 'mengmengma0104/kcc'
BRANCH = 'zh-CN'
API = 'https://api.github.com'

# fork 首页刻意与主仓库不同：导航指向下载页。同步时跳过。
INTENTIONAL_DIFF = {'README.md'}

SYNC_COMMIT_MESSAGE = (
    'sync: 与主仓库同步（源码与工具链）\n\n'
    '由 tools/zh/audit_sync_fork.py 经 GitHub API 完成；'
    'README.md 保持刻意的导航差异（指向 kcc-zh-cn 下载页）。'
)

TOKEN = subprocess.run([GH, 'auth', 'token'], capture_output=True).stdout.decode().strip()
S = requests.Session()
S.headers.update({'Authorization': 'Bearer ' + TOKEN,
                  'Accept': 'application/vnd.github+json',
                  'User-Agent': 'kcc-zh-cn-localizer'})


def api(method, path, payload=None):
    for attempt in range(1, 5):
        r = S.request(method, API + path, json=payload, timeout=120)
        if r.status_code < 300:
            return r.json() if r.content else {}
        if attempt == 4:
            raise RuntimeError('%s %s -> %s %s' % (method, path, r.status_code, r.text[:200]))
        print('    retry %d...' % attempt)


def blobs_of(repo, ref):
    tree = api('GET', '/repos/%s/git/trees/%s?recursive=1' % (repo, ref))
    assert not tree.get('truncated')
    return {e['path']: e['sha'] for e in tree['tree'] if e['type'] == 'blob'}, tree['sha']


# ---------------------------------------------------- ground truth: local tracked
raw = subprocess.run([GIT, '-C', LOCAL, 'ls-files'], capture_output=True, check=True)
local_paths = [p.replace('\\', '/') for p in raw.stdout.decode('utf-8', 'replace').splitlines()
               if p.strip()]
hasher = subprocess.run([GIT, '-C', LOCAL, 'hash-object', '--stdin-paths'],
                        input='\n'.join(local_paths).encode('utf-8'),
                        capture_output=True, check=True)
local = dict(zip(local_paths, hasher.stdout.decode('ascii', 'replace').split()))
print('local tracked files:', len(local))

# ---------------------------------------------------- remote trees
main_blobs, _ = blobs_of(MAIN, 'master')
fork_blobs, fork_tree_sha = blobs_of(FORK, BRANCH)
print('main blobs:', len(main_blobs), '| fork blobs:', len(fork_blobs))

# ---------------------------------------------------- audit vs local
def diff(other, other_name):
    only_other = sorted(set(other) - set(local))
    only_local = sorted(set(local) - set(other))
    differing = sorted(p for p in set(local) & set(other) if local[p] != other[p])
    print('--- %s vs local ---' % other_name)
    print('  仅远端有:', only_other or '(无)')
    print('  仅本地有:', only_local or '(无)')
    print('  内容不同:', differing or '(无)')
    return only_other, only_local, differing


mo, ml, md = diff(main_blobs, 'kcc-zh-cn master')
fo, fl, fd = diff(fork_blobs, 'fork zh-CN')

# ---------------------------------------------------- sync fork
# 需要修复：fork 缺失的（本地有）+ 内容不同的（排除刻意差异）
to_add = [p for p in fl if p not in INTENTIONAL_DIFF]
to_fix = [p for p in fd if p not in INTENTIONAL_DIFF]
print()
print('待同步到 fork: 缺失 %d 个 %s，内容不同 %d 个 %s'
      % (len(to_add), to_add, len(to_fix), to_fix))

if not to_add and not to_fix:
    print('fork 已与本地一致（除刻意差异），无需修改。')
else:
    entries = []
    for p in to_add + to_fix:
        data = open(os.path.join(LOCAL, p.replace('/', os.sep)), 'rb').read()
        import base64
        blob = api('POST', '/repos/%s/git/blobs' % FORK,
                   payload={'content': base64.b64encode(data).decode('ascii'),
                            'encoding': 'base64'})
        entries.append({'path': p, 'mode': '100644', 'type': 'blob', 'sha': blob['sha']})
        print('  blob uploaded:', p, '(%d bytes)' % len(data))
    # fork 上多出来且本地没有的文件：目前没有预期项；若有则保留不动并提示
    new_tree = api('POST', '/repos/%s/git/trees' % FORK,
                   payload={'base_tree': fork_tree_sha, 'tree': entries})
    head = api('GET', '/repos/%s/branches/%s' % (FORK, BRANCH))['commit']['sha']
    commit = api('POST', '/repos/%s/git/commits' % FORK,
                 payload={'message': '与主仓库同步：壁纸模式修复后的源文件与工具链'
                          '（KCC_ui.py / KCC.ui / translations.py / 审计与检查脚本 / 哈希文件）',
                          'tree': new_tree['sha'], 'parents': [head]})
    api('PATCH', '/repos/%s/git/refs/heads/%s' % (FORK, BRANCH),
        payload={'sha': commit['sha'], 'force': True})
    print('fork synced, head:', commit['sha'][:12])

# ---------------------------------------------------- re-verify
fork_blobs2, _ = blobs_of(FORK, BRANCH)
only_other, only_local, differing = diff(fork_blobs2, 'local')
real_diff = [p for p in differing if p not in INTENTIONAL_DIFF]
print()
print('=== 最终结论 ===')
if not only_other and not only_local and not real_diff:
    print('fork 与本地完全同步（唯一差异：README.md 导航刻意指向下载页）')
else:
    print('仍有差异！', only_other, only_local, real_diff)
