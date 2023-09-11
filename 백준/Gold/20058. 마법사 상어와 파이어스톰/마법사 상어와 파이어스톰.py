import sys
from collections import deque
input = sys.stdin.readline
N, Q = map(int, input().rstrip().split())
num = 2**N
arr = [list(map(int, input().rstrip().split())) for _ in range(num)]
Llist = list(map(int, input().rstrip().split()))
### 시계 방향 90도 회전 구현 함수
for l in Llist:
    for i in range(0, num, 2**l):
        for j in range(0,num, 2**l):
            change = [x[j:j+2**l] for x in arr[i:i+2**l]]
            newarr = [x[::-1] for x in list(map(list, zip(*change)))]
            for ci in range(2**l):
                for cj in range(2**l):
                    arr[i+ci][j+cj] = newarr[ci][cj]
    meltlst = []
    for qi in range(num):
        for qj in range(num):
            if arr[qi][qj] > 0:
                cnt = 0
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni,nj = qi+di, qj+dj
                    if 0<=ni<num and 0<=nj<num and arr[ni][nj] > 0:
                        cnt += 1
                if cnt<3:
                    meltlst.append((qi,qj))

    for ki,kj in meltlst:
        arr[ki][kj] -= 1

totalice, bigice = 0, 0
visited = [[0]*num for _ in range(num)]
for i in range(num):
    for j in range(num):
        totalice += arr[i][j]
        if arr[i][j] > 0:
            q = deque()
            q.append((i,j))
            cnt = 1
            visited[i][j] = 1
            while q:
                ci, cj = q.popleft()
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<num and 0<=nj<num and arr[ni][nj] > 0 and visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        cnt += 1
                        q.append((ni,nj))
            bigice = max(cnt, bigice)

print(totalice)
print(bigice)