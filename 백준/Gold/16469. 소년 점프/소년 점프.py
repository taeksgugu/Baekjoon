import sys
from collections import deque
input = sys.stdin.readline

### 필요한 값 입력 받기
R, C = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)]
nuksal_i, nuksal_j = map(lambda x: int(x)-1, input().rstrip().split())
swings_i, swings_j = map(lambda x: int(x)-1, input().rstrip().split())
changmo_i, changmo_j = map(lambda x: int(x)-1, input().rstrip().split())
dirlst = [(0,1), (0,-1), (1,0), (-1,0)]
### 넉살, 스윙스, 창모 이동경로 파악
visited1 = [[-1]*C for _ in range(R)]
visited2 = [[-1]*C for _ in range(R)]
visited3 = [[-1]*C for _ in range(R)]

def bfs(i,j, visited):
    q = deque()
    q.append((i,j))
    visited[i][j] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirlst:
            ni, nj = ci+di, cj+dj
            if 0<=ni<R and 0<=nj<C and arr[ni][nj] == '0' and visited[ni][nj] == -1:
                q.append((ni,nj))
                visited[ni][nj] = visited[ci][cj] + 1
    return visited

visited1 = bfs(nuksal_i, nuksal_j, visited1)
visited2 = bfs(swings_i, swings_j, visited2)
visited3 = bfs(changmo_i, changmo_j, visited3)

answer = R*C
cnt = 0
go = False
for i in range(R):
    for j in range(C):
        if arr[i][j] == '0' and visited1[i][j] != -1 and visited2[i][j] != -1 and visited3[i][j] != -1:
            num = max(visited1[i][j], visited2[i][j], visited3[i][j])
            go = True
            if num < answer and num != -1:
                # print(num, i, j)
                answer = num
                cnt = 1
            elif num == answer:
                cnt += 1

if not go:
    print(-1)
else:
    print(answer)
    print(cnt)