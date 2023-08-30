import sys
from collections import deque
input = sys.stdin.readline
N, M, T = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]
def bfs():
    q = deque()
    q.append((0,0))
    visited = [[0]*M for _ in range(N)]
    visited[0][0] = 1
    time = 1
    sword = float('INF')
    while q and time<=T:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in [(0,1), (0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if ni == N-1 and nj == M-1:
                    return min(time, sword)
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] != '1' and visited[ni][nj] == 0:
                    q.append((ni,nj))
                    visited[ni][nj] = 1
                    if arr[ni][nj] == '2':
                        sword = time + (N-ni-1) + (M-nj-1)
        time += 1
    if sword<=T:
        return sword
    return 'Fail'
print(bfs())