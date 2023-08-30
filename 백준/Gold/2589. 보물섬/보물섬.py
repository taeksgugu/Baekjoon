import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
answer = 0
def bfs(a,b):
    global answer
    q = deque([(a,b)])
    v2 = [[-1]*M for _ in range(N)]
    v2[a][b] = 0
    while q:
        i, j = q.popleft()
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and v2[ni][nj] == -1 and arr[ni][nj] == 'L':
                q.append((ni,nj))
                v2[ni][nj] = v2[i][j] + 1
    maxnum = v2[i][j]
    answer = max(answer, maxnum)
for x in range(N):
    for y in range(M):
        if arr[x][y] == 'L':
            bfs(x,y)

print(answer)