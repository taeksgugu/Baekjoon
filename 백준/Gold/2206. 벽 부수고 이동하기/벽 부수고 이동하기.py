import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int,input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[[0]*M for _ in range(N)] for _ in range(2)]

def bfs():
    queue = deque([(0,0,0)])
    visited[0][0][0] = 1
    visited[1][0][0] = 1
    while queue:
        i, j, broken = queue.popleft()
        if i == N-1 and j == M-1:
            return visited[broken][i][j]
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == '0' and visited[broken][ni][nj] == 0:
                    queue.append((ni,nj,broken))
                    visited[broken][ni][nj] = visited[broken][i][j] + 1
                if arr[ni][nj] == '1' and broken == 0 and visited[broken][ni][nj] == 0:
                    queue.append((ni,nj,1))
                    visited[1][ni][nj] = visited[broken][i][j] + 1
  
    return -1
print(bfs())