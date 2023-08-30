import sys
from collections import deque
input = sys.stdin.readline
F, S, G, U, D = map(int, input().rstrip().split())
if S < G and U == 0:
    print('use the stairs')
elif S > G and D == 0:
    print('use the stairs')
else:
    answer = 'use the stairs'
    visited = [0]*(F+1)
    queue = deque([(0,S)])
    visited[S] = 1
    while queue:
        n, stairs = queue.popleft()
        if stairs == G:
            answer = n
            break
        if stairs < G:
            lst = [U,-D]
        else:
            lst = [-D,U]
        for di in lst:
            nextstairs = stairs + di
            if 1<= nextstairs <= F and visited[nextstairs] == 0:
                queue.append((n+1, nextstairs))
                visited[nextstairs] = 1
    print(answer)