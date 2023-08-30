import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
### 주변 바다를 세서 빙산이 녹는걸 구현한 함수
def findsea():
    sealst = deque()
    icemountain = deque()
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0:
                cnt = 0
                for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0:
                        cnt += 1
                sealst.append((i,j,cnt))
    while sealst:
        i, j, cnt = sealst.popleft()
        arr[i][j] = max(0,arr[i][j]-cnt)
        if arr[i][j] > 0:
            icemountain.append((i,j))
    return icemountain

### 빙산 덩어리 세는 함수 만들기
def bfs(icemountain):
    visited = [[0]*M for _ in range(N)]
    answer = 0
    while icemountain:
        i, j = icemountain.popleft()
        if visited[i][j] == 0:
            answer += 1
        if answer >= 2:
            return answer
        q = deque([])
        q.append((i,j))
        visited[i][j] = 1
        while q:
            ci, cj = q.popleft()
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] > 0 and visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = 1
    return answer
year = 1

while True:
    lst = findsea()
    if lst:
        ans = bfs(lst)
        if ans >= 2:
            print(year)
            break
        else:
            year += 1
    else:
        print(0)
        break