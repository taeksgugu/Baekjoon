import heapq
def dijkstra(start):
    distance = [float('inf')] * N
    queue = []
    distance[start] = 0
    heapq.heappush(queue, [distance[start], start])
    while queue:
        # print(queue, distance)
        now_dist, now_node = heapq.heappop(queue)
        if distance[now_node] < now_dist: continue
        for new_node, new_dist in graph[now_node].items():
            if wardlst[new_node] == 0:
                dist = new_dist + now_dist
                if dist < distance[new_node]:
                    distance[new_node] = dist
                    heapq.heappush(queue, [dist, new_node])
    return distance

N, M = map(int, input().split())
graph = {n: {} for n in range(N)}
wardlst = list(map(int, input().split()))
wardlst[-1] = 0
for _ in range(M):
    start, end, distance = map(int, input().split())
    graph[start][end] = distance
    graph[end][start] = distance

answer = dijkstra(0)[-1]
if answer == float('inf'): print(-1)
else: print(answer)