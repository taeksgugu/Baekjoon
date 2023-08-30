import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
queue = []
for _ in range(M):
    s, e, d = map(int, input().rstrip().split())
    heapq.heappush(queue, [d, s, e])
parents = [i for i in range(N+1)]
def find(x):
    if parents[x]!=x:
        parents[x] = find(parents[x])
    return parents[x]
def union(a,b):
    parents[find(b)] = find(a)

answer = 0
while queue:
    dist, s, e = heapq.heappop(queue)
    if find(s) != find(e):
        answer += dist
        union(s,e)
print(answer)