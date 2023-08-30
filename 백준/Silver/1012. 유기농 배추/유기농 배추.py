### 초기 데이터 정리 (그래프, 방문리스트 등등)
T = int(input())

def dfs(node):
    node_i, node_j = node[0], node[1]
    visited[node_i][node_j] = 1
    for n in graph[str(node_i) + '*' + str(node_j)]:
        if visited[n[0]][n[1]] != 1:
            dfs(n)
for _ in range(T):
    M, N, K = map(int, input().split())
    arr = [[0]*(M+2)] + [[0]*(M+2) for _ in range(N)] + [[0]*(M+2)]
    visited = [[0]*(M+2)] + [[0]*(M+2) for _ in range(N)] + [[0]*(M+2)]
    graph = {}
    for _ in range(K):
        a, b = map(int, input().split())
        arr[b+1][a+1] = 1

    ### STack기반
    cabbagelst = []
    for i in range(1, N+1):
        for j in range(1, M+1):
            if arr[i][j] == 1:
                cabbagelst.append([i,j])
                cabbage_key = str(i)+'*'+str(j)
                if cabbage_key not in graph:
                    graph[cabbage_key] = []
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = i+di, j+dj
                    if arr[ni][nj] == 1:
                        graph[cabbage_key].append([ni,nj])
                        if str(ni) + '*' + str(nj) in graph:
                            graph[str(ni) + '*' + str(nj)].append([i,j])
                        else:
                            graph[str(ni) + '*' + str(nj)] = [[i,j]]

    cnt = 0
    for node in cabbagelst:
        xi, xj = node[0], node[1]
        if visited[xi][xj] != 1:
            cnt += 1
            dfs(node)

    print(cnt)