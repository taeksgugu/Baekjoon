from collections import deque
N, M = map(int, input().split())
visited = [0]*100001
q = deque([[N, 0]])
if N>M:
    print(N-M)
else:
    while q:
        now, step = q.popleft()
        if now == M:
            break
        if 0<=now<=100000 and visited[now] == 0:
            visited[now] = 1
            q.append([now + 1, step + 1])
            q.append([now - 1, step + 1])
            q.append([now * 2, step + 1])
    print(step)