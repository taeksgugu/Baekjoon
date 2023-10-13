import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = [list(input()) for _ in range(M)]
visited = [[[0]*N for _ in range(M)] for _ in range(4)]
cnt = 0
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]
for i in range(M):
    for j in range(N):
        if arr[i][j] == '.': ## 비로소 탐색 시작 가능
            for idx in range(4):
                di, dj = dirlst[idx]
                ni, nj = i+di, j+dj
                if 0<=ni<M and 0<=nj<N and arr[ni][nj]=='X':
                    # print(idx, i, j)
                    visited[idx][i][j] = 1

checkdir = [(0,1), (1,0)]
wallchk = {0:[0,1], 1:[2,3]}
for i in range(M):
    for j in range(N):
        if arr[i][j] == '.':
            for cidx in range(2):
                di, dj = checkdir[cidx]
                ni, nj = i+di, j+dj
                if 0<=ni<M and 0<=nj<N and arr[ni][nj]=='.':
                    if visited[wallchk[cidx][0]][i][j] == 1 and visited[wallchk[cidx][0]][ni][nj] == 1:
                        cnt += 1
                        visited[wallchk[cidx][0]][i][j] = 0
                        visited[wallchk[cidx][0]][ni][nj] = 0
                    if visited[wallchk[cidx][1]][i][j] == 1 and visited[wallchk[cidx][1]][ni][nj] == 1:
                        cnt += 1
                        visited[wallchk[cidx][1]][i][j] = 0
                        visited[wallchk[cidx][1]][ni][nj] = 0
print(cnt)

