import sys
from collections import deque
input = sys.stdin.readline

### 입력 받기
N = int(input())
arr = [[0]*N for _ in range(N)]
visited = [[0]*N if i%2==1 else [0]*(N-1) for i in range(1,N+1)]
distarr = [[0]*N for _ in range(N)] ### 거리 정리
idx = 1
tilenumpos = {}
tilenumpos[0] = (-1,-1) ### 없음
for i in range(N):
    if i%2==0: length = N
    else: length = N-1
    for j in range(length):
        arr[i][j] = idx
        tilenumpos[idx] = (i,j)
        idx += 1


tiledict = {}
tiledict[0] = (-1,-1)
for num in range(1, idx):
    tiledict[num] = list(map(int, input().split()))

odd_dirlst = [(-1,0), (1,0), (0,-1), (-1,1), (1,1), (0,1)]
even_dirlst = [(-1,-1), (1,-1), (0,-1), (-1,0), (1,0), (0,1)]
def bfs():
    visited[0][0] = 'start'
    distarr[0][0] = 1
    q = deque()
    q.append((0,0))
    while q:
        ci, cj = q.popleft()
        if ci%2==0: dirlst = even_dirlst
        else: dirlst = odd_dirlst
        for diridx in range(6):
            di, dj = dirlst[diridx]
            ni, nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<N: ### 격자 내
                if diridx <= 2:
                    if tiledict[arr[ci][cj]][0] == tiledict[arr[ni][nj]][1] and visited[ni][nj] == 0:
                        visited[ni][nj] = (ci,cj)
                        distarr[ni][nj] = distarr[ci][cj] + 1
                        q.append((ni,nj))
                else:
                    if tiledict[arr[ci][cj]][1] == tiledict[arr[ni][nj]][0] and visited[ni][nj] == 0:
                        visited[ni][nj] = (ci,cj)
                        distarr[ni][nj] = distarr[ci][cj] + 1
                        q.append((ni,nj))

    for ei in range(N-1,-1,-1):
        for ej in range(N-1,-1,-1):
            if distarr[ei][ej] != 0: ### 제일 큰 타일번호
                routeq = deque()
                routeq.append((ei, ej))
                routelst = [arr[ei][ej]]
                while routeq:
                    ci, cj = routeq.popleft()
                    ni, nj = visited[ci][cj]
                    routeq.append((ni, nj))
                    routelst.append(arr[ni][nj])
                    if ni == 0 and nj == 0: return routelst


# for l in arr:
#     print(*[tiledict[x] for x in l])
if N == 1:
    print(1)
    print(1)
else:
    route = bfs()
    print(len(route))
    print(*route[::-1])
