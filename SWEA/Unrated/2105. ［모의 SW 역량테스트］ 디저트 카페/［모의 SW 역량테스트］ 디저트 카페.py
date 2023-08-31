def dfs(n, i, j, idx):
    global answer
    if n>=4 and i==start_i+1 and j==start_j-1 and idx>=2:
        answer = max(answer, n)
        return
    for qq in range(idx, min(4,idx+2)):
        di, dj = dirlst[qq]
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and dessert[arr[ni][nj]] == 0: ## 지도에서 안 나가고, 방문한 적 없고 디저트도 먹어본 적 없는 디저트일 때
            visited[ni][nj] = 1
            dessert[arr[ni][nj]] = 1
            dfs(n+1, ni, nj, qq)
            visited[ni][nj] = 0
            dessert[arr[ni][nj]] = 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    dirlst = [(1,1),(1,-1),(-1,-1),(-1,1)] ### 대각선 움직이는 방향
    answer = -1
    for ci in range(N):
        for cj in range(N):
            if (ci==0 and cj==0) or (ci==N-1 and cj==N-1) or (ci==N-1 and cj==0) or (ci==0 and cj==N-1):
                continue
            visited = [[0]*N for _ in range(N)]
            dessert = [0] * 101
            start_i, start_j = ci, cj
            visited[ci][cj] = 1
            dessert[arr[ci][cj]] = 1
            dfs(1,ci,cj,0)
    print(f"#{tc} {answer}")