import sys
from collections import deque
input = sys.stdin.readline
K = int(input().rstrip())
W, H = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(H)]
visited = [[[-1]*W for _ in range(H)] for _ in range(K+1)]
def bfs():
    time = 0
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 1
    while q:
        for _ in range(len(q)):
            i, j, cnt = q.popleft()
            ### 원숭이처럼 인접한 칸 이동
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = i + di, j + dj
                if ni == H - 1 and nj == W - 1:
                    return time+1
                if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == '0' and visited[cnt][ni][nj]==-1:
                    q.append((ni, nj, cnt))
                    visited[cnt][ni][nj] = 1
            if cnt < K:
                for di, dj in [(-1, -2), (-2, -1), (-2, 1), (-1, 2), (1, -2), (2, -1), (2, 1), (1, 2)]:
                    ni, nj = i + di, j + dj
                    if ni == H - 1 and nj == W - 1:
                        return time+1
                    if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] == '0' and visited[cnt+1][ni][nj]==-1:
                        q.append((ni, nj, cnt + 1))
                        visited[cnt+1][ni][nj] = 1
        time += 1
    return -1
if W == 1 and H == 1:
    print(0)
else:
    print(bfs())
    # for l in visited:
    #     print(*l)