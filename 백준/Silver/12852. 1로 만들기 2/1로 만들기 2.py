import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
visited = [0]*(N+1)
def solve():
    q = deque([(N,0,[N])])
    visited[N] = 1
    while q:
        num, cnt, lst = q.popleft()
        if num == 1:
            return cnt, lst

        if num%3 == 0 and visited[num//3] == 0:
            q.append((num//3, cnt+1, lst+[num//3]))
            visited[num//3] = 1
        if num%2 == 0 and visited[num//2] == 0:
            q.append((num//2, cnt+1, lst+[num//2]))
            visited[num//2] = 1
        if visited[num-1] == 0:
            q.append((num-1, cnt+1, lst+[num-1]))
            visited[num-1] = 1
a, b = solve()
print(a)
print(*b)