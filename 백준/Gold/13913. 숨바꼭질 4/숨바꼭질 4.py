from collections import deque
N, M = map(int, input().split())
visited = [False]*100001
visited[N] = N
q = deque([[N, 0, [N]]])
if N > M:
    print(N-M)
    print(*[int(x) for x in range(N, M-1, -1)])
else:
    while q:
        now, step, road = q.popleft()
        if now == M:
            print(step)
            print(*road)
            break
        for alpha in [now+1, now-1, now*2]:
            if 0<=alpha<=100000 and visited[alpha] == False:
                visited[alpha] = True
                newroad = road + [alpha]
                q.append([alpha, step + 1, newroad])