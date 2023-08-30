import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    graph[b].append(a)
def bfs(number):
    cnt = 1
    q = deque([number])
    visited = [0] * (N+1)
    visited[number] = 1

    while q:
        for _ in range(len(q)):
            n = q.popleft()

            for num in graph[n]:
                if visited[num] == 0:
                    q.append(num)
                    visited[num] = 1
                    cnt += 1
    return cnt
answer = 0
answerlst = []
for i in range(1, N+1):
    computer = bfs(i)
    # print(i, computer)
    if computer > answer:
        answer = computer
        answerlst = [i]
    elif computer == answer:
        answerlst.append(i)
print(*sorted(answerlst))