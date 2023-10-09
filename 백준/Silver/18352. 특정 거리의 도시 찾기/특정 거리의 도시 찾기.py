import sys, heapq
input = sys.stdin.readline

def dijkstra(start):
    distance = [1e9] * (N + 1)
    distance[start] = 0
    q = []
    heapq.heappush(q, (distance[start], start))
    while q:
        now_dist, now_node = heapq.heappop(q)
        if distance[now_node] < now_dist: continue

        for new_node, new_dist in graph[now_node].items():
            dist = new_dist + now_dist
            if dist < distance[new_node]:
                distance[new_node] = dist
                heapq.heappush(q, (dist, new_node))
    return distance
N, M, K, X = map(int, input().split())
graph = {n:{} for n in range(1, N+1)}
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = 1

anslst = dijkstra(X)
if K not in anslst:
    print(-1)
else:
    for idx in range(1, N+1):
        if anslst[idx] == K:
            print(idx)