import sys
from collections import deque
input = sys.stdin.readline
arr = []
N, M = map(int, input().rstrip().split())
### 연구실 입력 및 바이러스 위치 리스트 생성
viruslst = []
emptycnt = 0
for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    for j in range(N):
        if lst[j] == 2:
            viruslst.append((i,j))
        elif lst[j] == 0:
            emptycnt += 1
    arr.append(lst)
### 조합 수 만들기
comblst = []
def comb(n, lst, idx):
    if n==M:
        comblst.append(lst)
        return
    for i in range(idx+1, len(viruslst)):
        comb(n+1, lst+[viruslst[i]], i)
comb(0,[],-1)
def bfs():
    unactive = []
    delcnt = emptycnt
    q = deque(active)
    visited = [['-']*N for _ in range(N)]
    for i, j in q:
        visited[i][j] = 0
    while q:
        i, j = q.popleft()
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and (visited[ni][nj] == '-'):
                if arr[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    delcnt -= 1
                    q.append((ni,nj))
                elif arr[ni][nj] == 2:
                    visited[ni][nj] = visited[i][j] + 1
                    unactive.append((ni,nj))
                    q.append((ni,nj))
    for i, j in unactive:
        visited[i][j] = '-'
    # print(active, delcnt, max(x if x!='-' else 0 for y in visited for x in y))
    if delcnt == 0:
        return max(x if x!='-' else 0 for y in visited for x in y)
    return -1

answerlst = []
for active in comblst:
    ans = bfs()
    if ans != -1:
        answerlst.append(ans)
if answerlst:
    print(min(answerlst))
else:
    print(-1)