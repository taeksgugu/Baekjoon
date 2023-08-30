import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
def bfs():
    q = deque()
    visited =[0]*100001
    q.append(N)
    visited[N] == 1
    time = 0
    cnt = 0
    if N == K:
        print(0)
        print(1)
        return
    while q:
        # print(q, cnt)
        for _ in range(len(q)):
            num = q.popleft()
            for di in [-1, 1, num]:
                num2 = num + di
                if num2 == K:
                    cnt += 1
                elif 0<=num2<100001 and (visited[num2]==0 or visited[num2]==time):
                    q.append(num2)
                    visited[num2] = time
        time += 1
        if cnt > 0:
            print(time)
            print(cnt)
            return
bfs()
