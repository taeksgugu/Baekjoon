import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
graph = [0 for _ in range(N+1)]
arr2 = []
for i in range(1, N+1):
    num = int(input().rstrip())
    graph[i] = num
    arr2.append(num)
arr1 = [i for i in range(1,N+1) if i in arr2]
arr2 = list(set([arr2[i-1] for i in arr1]))
answer = []
for i in arr2:
    lst = []
    visited = [0] * (N + 1)
    if visited[i] == 0 and i not in answer:
        lst.append(i)
        q = deque([i])
        visited[i] = 1
        while q:
            node = q.pop()
            if visited[graph[node]] == 0:
                visited[graph[node]] = 1
                if graph[node] in arr2:
                    q.append(graph[node])
                    lst.append(graph[node])
                else:
                    break
    if graph[node] == i:
        answer += lst
        # print(i, graph[node], lst)
print(len(answer))
for ans in sorted(answer):
    print(ans)