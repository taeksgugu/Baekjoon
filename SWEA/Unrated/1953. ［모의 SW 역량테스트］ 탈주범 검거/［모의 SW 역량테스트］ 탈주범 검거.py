from collections import deque
dirdict = {1:[(-1,0), (1,0), (0,-1), (0,1)], 2: [(-1,0), (1,0)], 3: [(0,-1), (0,1)], 4: [(-1,0), (0,1)], 5: [(1,0), (0,1)], 6: [(1,0), (0,-1)], 7:[(-1,0), (0,-1)]}
cango = {(-1,0): [1,2,5,6], (1,0): [1,2,4,7], (0,-1):[1,3,4,5], (0,1):[1,3,6,7]}
T = int(input())
for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    q = deque()
    q.append((R,C))
    visited[R][C] = 1
    time = 1
    while q:
        if time==L: break
        time += 1
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in dirdict[arr[ci][cj]]:
                ni, nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] in cango[(di,dj)] and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    q.append((ni,nj))

    ### 디버깅
    # for l in visited:
    #     print(*l)
    print(f"#{tc} {sum(map(sum, visited))}")