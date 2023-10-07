import sys
from collections import deque
input = sys.stdin.readline

N, K, M = map(int, input().split())
graph = {n:[] for n in range(1,N+1)}
tubedata = []
for num in range(M):
    tubelst = list(map(int, input().split()))
    tubedata.append(tubelst)
    for station in tubelst:
        graph[station].append(num)

### 디버깅
# for k,v in graph.items():
#     print(k,v)
# print()
# print(tubedata)

def solve():
    v = [0]*(N+1)
    q = deque()
    q.append(1)
    v[1] = 1
    while q:
        num = q.popleft()
        for hypertubenum in graph[num]:
            for next in tubedata[hypertubenum]:
                if v[next] == 0:
                    v[next] = v[num] + 1
                    q.append(next)
                    if next == N: return v[next]

    return -1

if N==1: print(1)
else: print(solve())