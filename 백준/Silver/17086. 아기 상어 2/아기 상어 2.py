N, M = map(int, input().split())
arr = [input().split() for _ in range(N)]
answerarr = [[100]*M for _ in range(N)]
checklst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1':
            answerarr[i][j] = 0
            checklst.append([i,j,0])
answer = 0
for check in checklst:
    willvisit = [check]
    visited = [[0]*M for _ in range(N)]
    while willvisit:
        node_i, node_j, step = willvisit.pop(0)
        if visited[node_i][node_j] != 1:
            visited[node_i][node_j] = 1
            answerarr[node_i][node_j] = min(answerarr[node_i][node_j], step)
            for di, dj in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
                ni, nj = node_i+di, node_j+dj
                if 0<=ni<N and 0<=nj<M and visited[ni][nj] != 1:
                    willvisit.append([ni,nj,step+1])
print(max([x for y in answerarr for x in y]))