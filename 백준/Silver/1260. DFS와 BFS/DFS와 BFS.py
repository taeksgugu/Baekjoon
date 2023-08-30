N, M, start = map(int, input().split())
graph = [[] for _ in range(N+1)]
visited_dfs = [0]*(N+1)
visited_bfs = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
graph = [sorted(x) for x in graph]
answer_dfs, answer_bfs = [],[]
### DFS
def dfs(node):
    visited_dfs[node] = 1
    answer_dfs.append(node)
    for n in graph[node]:
        if visited_dfs[n] != 1:
            dfs(n)
dfs(start)
### BFS
willvisit = [start]
while willvisit:
    node = willvisit.pop(0)
    if visited_bfs[node] != 1:
        visited_bfs[node] = 1
        answer_bfs.append(node)
        willvisit.extend(graph[node])
print(*answer_dfs)
print(*answer_bfs)