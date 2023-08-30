import sys
from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(N)]
visited = [[K+1]*M for _ in range(N)]
def solve():
    q = deque([(0,0,1)])
    visited[0][0] = 0
    while q:
        i, j, cnt = q.popleft()
        broken = visited[i][j]
        if i == N-1 and j == M-1:
            return cnt
        if broken > K:
            continue
        for di, dj in [(0,1), (0,-1), (1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M:
                if broken<=K-1 and arr[ni][nj] == '1' and visited[ni][nj] > broken+1:
                    q.append((ni,nj, cnt+1))
                    visited[ni][nj] = broken+1
                if arr[ni][nj] == '0' and visited[ni][nj] > broken:
                    q.append((ni,nj, cnt+1))
                    visited[ni][nj] = broken
    return -1
print(solve())