import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
newarr = arr[::]
spacelst = []
cnt = 0
casecnt = 0
def dfs(i,j):
    queue = deque([(i,j)])
    visited[i][j] = 2
    while queue:
        node_i, node_j = queue.popleft()
        visited[node_i][node_j] = 2
        for di, dj in [(0,1), (0,-1), (1,0),(-1,0)]:
            ni, nj = node_i+di, node_j+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                queue.append((ni,nj))
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            cnt += 1
            spacelst.append((i,j))

for a in range(cnt):
    for b in range(a+1, cnt):
        for c in range(b+1, cnt):
            case = cnt
            wx1, wy1 = spacelst[a]
            wx2, wy2 = spacelst[b]
            wx3, wy3 = spacelst[c]
            arr[wx1][wy1] = 1
            arr[wx2][wy2] = 1
            arr[wx3][wy3] = 1
            visited = [[0]*M for _ in range(N)]
            for i in range(N):
                for j in range(M):
                    if arr[i][j] == 2:
                        case += 1
                        dfs(i,j)
            for i in range(N):
                for j in range(M):
                    if visited[i][j] == 2:
                        case -= 1
            # if case > casecnt and case>=29:
            #     print(wx1,wy1, wx2,wy2,wx3,wy3)
            #     print(case)
            #     for pp in arr:
            #         print(pp)
            #     print()
            #     for l in visited:
            #         print(l)
            #     print()
            arr[wx1][wy1] = 0
            arr[wx2][wy2] = 0
            arr[wx3][wy3] = 0


            casecnt = max(casecnt, case-3)

print(casecnt)