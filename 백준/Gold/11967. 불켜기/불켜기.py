import sys
from collections import deque, defaultdict
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    sr, sc, tr, tc = map(int, input().split())
    graph[(sr - 1, sc - 1)].append((tr - 1, tc - 1))

cnt = 1
visited = [[0] * N for _ in range(N)]
ledmap = [[0] * N for _ in range(N)]
ledmap[0][0] = 1
q = deque([(0, 0)])
visited[0][0] = 1

while q:
    r, c = q.popleft()
    for tr, tc in graph[(r, c)]:
        if not ledmap[tr][tc]:
            ledmap[tr][tc] = 1
            cnt += 1
            for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = tr + di, tc + dj
                if not (0 <= nr < N and 0 <= nc < N):
                    continue
                if visited[nr][nc]:
                    q.append((nr, nc))

    # 현 위치를 기준으로
    for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nr, nc = r + di, c + dj
        if not (0 <= nr < N and 0 <= nc < N):
            continue
        if not visited[nr][nc] and ledmap[nr][nc]:
            q.append((nr, nc))  # 재검사를 위해 큐에 담기
            visited[nr][nc] = 1  # 방문 표시

print(cnt)