### 초기 그래프 생성 및 방문리스트 생성
N = int(input())
graph = [[] for _ in range(N+1)]
M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (N+1)
### stack 풀이 과정
# from collections import deque
# willvisit = [1]
# while willvisit:
#     node = willvisit.pop()
#     if visited[node] != 1:
#         visited[node] = 1
#         willvisit.extend(graph[node])
#
# print(sum(visited)-1)

### 재귀 풀이 과정
def dfs(node):
    visited[node] = 1
    answer.append(node)
    for n in graph[node]:
        if visited[n] != 1:
            dfs(n)

answer = []
dfs(1)
print(len(answer)-1)
