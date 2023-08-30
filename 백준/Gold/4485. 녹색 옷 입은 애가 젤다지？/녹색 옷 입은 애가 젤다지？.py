import sys, heapq
input = sys.stdin.readline
tc = 1
while True:
    N = int(input().rstrip())
    if N == 0:
        break
    arr = [list(map(int,input().rstrip().split())) for _ in range(N)]
    visited = [[10*N*N]*N for _ in range(N)]
    visited[0][0] = arr[0][0]
    queue = []
    heapq.heappush(queue,(visited[0][0],0,0))

    while queue:
        now_dist, now_x, now_y = heapq.heappop(queue)
        if visited[now_x][now_y] < now_dist:
            continue
        for di,dj in [(-1,0),(1,0),(0,-1), (0,1)]:
            ni, nj = now_x+di, now_y+dj
            if 0<=ni<N and 0<=nj<N:
                newdist = now_dist + arr[ni][nj]
                if newdist < visited[ni][nj]:
                    visited[ni][nj] = newdist
                    heapq.heappush(queue,(newdist, ni, nj))
    print(f"Problem {tc}: {visited[-1][-1]}")
    tc += 1