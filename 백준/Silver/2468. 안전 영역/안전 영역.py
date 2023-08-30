import sys
sys.setrecursionlimit(10000)
N = int(input())
min_height, max_height = 1, 100
arr = []
for _ in range(N):
    lst = list(map(int, input().split()))
    arr.append(lst)
    min_height = min(min_height, min(lst))
    max_height = max(max_height, max(lst))

def dfs(node):
    node_i, node_j = node[0], node[1]
    visited[node_i][node_j] = 1
    for n in graph[str(node_i)+'*'+str(node_j)]:
        if visited[n[0]][n[1]] != 1:
            dfs(n)

answer = 0
for height in range(min_height-1,max_height+1):
    cnt = 0
    graph = {}
    visited = [[0]*N for _ in range(N)]
    checklst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] > height:
                checklst.append([i,j])
                lst = []
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]>height:
                        lst.append([ni,nj])
                graph[str(i) + '*' + str(j)] = lst

    for node in checklst:
        if visited[node[0]][node[1]] != 1:
            cnt += 1
            dfs(node)
    answer = max(answer, cnt)
print(answer)