### 재귀
import sys
sys.setrecursionlimit(10000)
M, N, K = map(int, input().split())
arr = [[1]*(N+2)] + [[1] + [0]*N + [1] for _ in range(M)] + [[1]*(N+2)]
for _ in range(K):
    a, b, c, d = map(int, input().split())
    for i in range(b+1,d+1):
        for j in range(a+1, c+1):
            arr[i][j] = 1
visited = [[0]*(N+2) for _ in range(M+2)]
graph = {}
checklst = []
cnt = 0
sizelst = []
for i in range(1, M+1):
    for j in range(1, N+1):
        if arr[i][j] == 0:
            checklst.append([i,j])
            graph[str(i)+'*'+str(j)] = []
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i+di, j+dj
                if arr[ni][nj] == 0:
                    graph[str(i)+'*'+str(j)].append([ni,nj])
                    if str(ni)+'*'+str(nj) in graph:
                        graph[str(ni)+'*'+str(nj)].append([i,j])
                    else:
                        graph[str(ni)+'*'+str(nj)] = [[i,j]]

def dfs(node):
    global size
    node_i, node_j = node[0], node[1]
    visited[node_i][node_j] = 1
    size += 1
    for n in graph[str(node_i)+'*'+str(node_j)]:
        if visited[n[0]][n[1]] != 1:
            dfs(n)
for node in checklst:
    if visited[node[0]][node[1]] != 1:
        size = 0
        cnt += 1
        dfs(node)
        sizelst.append(size)

sizelst.sort()
print(cnt)
print(*sizelst)