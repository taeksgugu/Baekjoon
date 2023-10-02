import sys
from collections import deque
input = sys.stdin.readline
N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
answer = [[0] * M for _ in range(N)]

for i in range(min(N, M)//2):
    q = deque()
    q.extend(arr[i][i:M-i])
    q.extend([x[M-i-1] for x in arr[i+1:N-i-1]])
    q.extend(arr[N-i-1][i:M-i][::-1])
    q.extend([x[i] for x in arr[i+1:N-i-1]][::-1])
    ### 디버깅
    # print(q)
    q.rotate(-R)
    # print(q)
    for j in range(i, M-i): answer[i][j] = q.popleft()
    for j in range(i+1, N-i-1): answer[j][M-i-1] = q.popleft()
    for j in range(M-i-1, i-1, -1): answer[N-i-1][j] = q.popleft()
    for j in range(N-i-2, i, -1): answer[j][i] = q.popleft()

for l in answer:
    print(*l)