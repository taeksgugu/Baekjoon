import sys
from collections import deque
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [['*']*M for _ in range(N)]
for _ in range(K):
    a, b = map(lambda x: int(x)-1, input().split())
    arr[a][b] = '#'

answer = 0
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == '#' and visited[i][j] == 0:
            cnt = 1
            q = deque()
            q.append((i,j))
            visited[i][j] = 1
            while q:
                ci, cj = q.popleft()
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '#' and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        q.append((ni,nj))
                        cnt += 1
            answer = max(answer, cnt)
print(answer)