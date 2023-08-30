def dfs(n, idx):
    global answer
    if answer==1:
        return
    if n==5:
        answer = 1
        return
    for num in graph[idx]:
        if visited[num] == 0:
            visited[num] = 1
            dfs(n+1, num)
            visited[num] = 0

N, M = map(int ,input().rstrip().split())
graph = [[] for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [0] * (N)
answer = 0
for k in range(N):
    visited[k] = 1
    dfs(1,k)
    visited[k] = 0
print(answer)