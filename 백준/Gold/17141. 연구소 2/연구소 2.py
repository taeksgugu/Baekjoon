import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
viruslst = []
emptycnt = N*N
for i in range(N):
    for j in range(N):
        if arr[i][j] == 2:
            viruslst.append((i,j))
            arr[i][j] = 0
        elif arr[i][j] == 1: emptycnt -= 1

def bfs(lst):
    remain = emptycnt - M
    visited =[[-1]*N for _ in range(N)]
    q = deque(lst)
    for hi,hj in lst:
        visited[hi][hj] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = ci+di ,cj+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and visited[ni][nj] == -1:
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni,nj))
                remain -= 1
    # for l in visited:
    #     print(*l)
    if remain == 0: return True, max(map(max, visited))
    else: return False, -1

answer = 1e9
def makecomb(n, idx, lst):
    global answer
    if n == M:
        cango, time = bfs(lst)
        # print(lst, cango, time)
        if cango: answer = min(answer, time)
        return

    for i in range(idx+1, len(viruslst)):
        makecomb(n+1, i, lst+[viruslst[i]])

makecomb(0,-1,[])
if answer == 1e9: print(-1)
else: print(answer)