import sys
from collections import deque
M, N, H = map(int, input().rstrip().split())
q = deque()
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
arr = []
cnt = 0
for i in range(H):
    h_lst = []
    for j in range(N):
        lst = input().rstrip().split()
        for k in range(M):
            if lst[k] == '0':
                cnt += 1
            elif lst[k] == '1':
                q.append((i,j,k))
                visited[i][j][k] = 1
        h_lst.append(lst)
    arr.append(h_lst)
def bfs():
    global cnt
    while q:
        i,j,k = q.popleft()
        for di,dj,dk in ((-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)):
            ni,nj,nk = i+di, j+dj, k+dk
            if 0 <= ni < H and 0 <= nj < N and 0 <= nk < M and visited[ni][nj][nk] == 0 and arr[ni][nj][nk] == '0':
                q.append((ni, nj, nk))
                visited[ni][nj][nk] = visited[i][j][k] + 1
                cnt -= 1

    if cnt>0:
        return -1
    else:
        return visited[i][j][k]-1
print(bfs())