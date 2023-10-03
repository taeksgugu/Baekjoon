import sys
input = sys.stdin.readline


K, N, F = map(int, input().split())
graph = {n:[] for n in range(1, N+1)}
for _ in range(F):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

def choose(idx,lst):
    if len(lst) == K:
        for num in lst:
            print(num)
        exit()
    for i in range(idx+1,N+1):
        if not visited[i]:
            for num in lst:
                if num not in graph[i]: break
            else:
                visited[i] = True
                choose(i,lst+[i])


for start in range(1, N+1):
    visited = [0] * (N + 1)
    visited[start] = 1
    choose(start, [start])
    
print(-1)