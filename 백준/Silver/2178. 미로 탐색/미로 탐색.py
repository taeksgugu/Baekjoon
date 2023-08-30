N, M = map(int, input().split())
arr = ['0'*(M+2)]+['0'+input()+'0' for _ in range(N)]+['0'*(M+2)]
visited = [[0]*(M+2) for _ in range(N+2)]
willvisit = [[1,1,1]]
while willvisit:
    node_i, node_j, step = willvisit.pop(0)
    if node_i == N and node_j == M:
        answer = step
        break
    if visited[node_i][node_j] != 1:
        visited[node_i][node_j] = 1
        neighbor = []
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = node_i+di, node_j+dj
            if arr[ni][nj] == '1':
                neighbor.append([ni,nj,step+1])
        willvisit.extend(neighbor)
print(answer)

