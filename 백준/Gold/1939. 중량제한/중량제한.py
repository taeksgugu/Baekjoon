import heapq, sys
input = sys.stdin.readline
def dijkstra(start):
    distance = [0] * (N+1)
    queue = []
    distance[start] = -1e11
    heapq.heappush(queue, [distance[start], start])
    while queue:
        now_dist, now_node = heapq.heappop(queue)
        if distance[now_node] < now_dist:
            continue
        for new_node, new_dist in graph[now_node].items():
            dist = max(new_dist, now_dist)
            if dist < distance[new_node]:
                distance[new_node] = dist
                heapq.heappush(queue, [dist, new_node])
    return distance


N, M = map(int, input().split())
graph = {n: {} for n in range(N+1)}
for _ in range(M):
    start, end, distance = map(int, input().split())
    graph[start][end] = distance*(-1)
    graph[end][start] = distance*(-1)
start, end = map(int, input().rstrip().split())
print(dijkstra(start)[end]*(-1))