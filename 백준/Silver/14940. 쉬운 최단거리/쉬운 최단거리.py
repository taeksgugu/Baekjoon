import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = []
for i in range(N):
    lst = input().rstrip().split()
    for j in range(M):
        if lst[j] == '2':
            a, b = i,j
            break
    arr.append(lst)
visited = [[-1]*M for _ in range(N)]
def bfs(a,b):
    q = deque([(a,b)])
    visited[a][b] = 0
    while q:
        i, j = q.popleft()
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] == -1:
                if arr[ni][nj] == '0':
                    visited[ni][nj] = 0
                else:
                    q.append((ni,nj))
                    visited[ni][nj] = visited[i][j] + 1
bfs(a,b)
for i in range(N):
    for j in range(M):
        if arr[i][j] == '0' and visited[i][j] == -1:
            visited[i][j] = 0
for l in visited:
    print(*l)