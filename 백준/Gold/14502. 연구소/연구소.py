import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = []
viruslst = []
emptylst = []
emptycnt = 0
for i in range(N):
    line = input().rstrip().split()
    for j in range(M):
        if line[j] == '2':
            viruslst.append((i,j))
        elif line[j] == '0':
            emptylst.append((i,j))
            emptycnt += 1
    arr.append(line)
### 안전구역 계산
def bfs(lst):
    global answer
    q = deque(viruslst)
    visited = [[0]*M for _ in range(N)]
    newcnt = emptycnt-3
    for i,j in q:
        visited[i][j] = 1
    for vi,vj in lst:
        visited[vi][vj] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='0' and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = 1
                newcnt -= 1
    answer = max(answer, newcnt)

### 벽 세우는 경우의 수 만들기
answer = 0
def dfs(n, idx, lst):
    if n == 3:
        bfs(lst)
        return
    for i in range(idx+1, emptycnt):
        dfs(n+1, i, lst+[emptylst[i]])
dfs(0,-1,[])
print(answer)