import sys
from collections import deque
input = sys.stdin.readline

### 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
islandarr = [[0]*N for _ in range(N)]
cnt = 0
islanddict = {}
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1 and islandarr[i][j] == 0:
            cnt += 1
            group = set()
            q = deque()
            q.append((i,j))
            islandarr[i][j] = cnt
            while q:
                ci, cj = q.popleft()
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<N and 0<=nj<N:
                        if arr[ni][nj] == 1 and islandarr[ni][nj] == 0:
                            islandarr[ni][nj] = cnt
                            q.append((ni,nj))
                        if arr[ni][nj] == 0:
                            group.add((ci,cj))
            islanddict[cnt] = group

answer = 1e9

for s1 in range(1, cnt+1):
    for s2 in range(s1+1, cnt+1):
        for ki, kj in islanddict[s1]:
            for pi, pj in islanddict[s2]:
                dist = abs(ki-pi)+abs(kj-pj)-1
                answer = min(dist, answer)
print(answer)