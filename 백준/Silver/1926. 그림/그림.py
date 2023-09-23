import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

### 그림 확인 및 최대 넓이 구하기
picturecnt, picturesize = 0, 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            picturecnt += 1
            cnt = 0
            q = deque()
            q.append((i,j))
            visited[i][j] = 1
            while q:
                ci, cj = q.popleft()
                cnt += 1
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and visited[ni][nj] == 0:
                        q.append((ni,nj))
                        visited[ni][nj] = 1

            picturesize = max(picturesize, cnt)

print(picturecnt)
print(picturesize)