T = int(input())
for _ in range(T):
    N = int(input())
    start_i, start_j = map(int, input().split())
    end_i, end_j = map(int, input().split())
    willvisit = [[end_i, end_j, 0]]
    visited = [[0]*N for _ in range(N)]
    while willvisit:
        node_i, node_j, step = willvisit.pop(0)
        if node_i == start_i and node_j == start_j:
            answer = step
            break
        if visited[node_i][node_j] != 1:
            visited[node_i][node_j] = 1
            for di, dj in [(-2,-1), (-2,1), (-1,-2), (-1,2), (1,-2), (1,2), (2,-1), (2,1)]:
                ni, nj = node_i+di, node_j+dj
                if 0<=ni<N and 0<=nj<N and visited[ni][nj] != 1:
                    willvisit.append([ni,nj,step+1])
    print(answer)