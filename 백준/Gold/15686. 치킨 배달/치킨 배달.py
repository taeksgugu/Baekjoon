import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = []
chickenlst = []
homelst = []
housecnt = 0
for i in range(N):
    lst = input().rstrip().split()
    for j in range(N):
        if lst[j] == '2':
            chickenlst.append((i,j))
            housecnt += 1
        elif lst[j] == '1':
            homelst.append((i,j))
    arr.append(lst)
answer = N**3
### 도시 치킨 거리 구하기
def bfs(case):
    cnt = 0
    for i, j in homelst:
        distlst = [abs(ci-i)+abs(cj-j) for ci, cj in case]
        cnt += min(distlst)
    return cnt
### 치킨 집 조합 구하기
def makecomb(n, idx, lst):
    global answer
    if n == M:
        casedist = bfs(lst)
        answer = min(casedist, answer)
        return
    for i in range(idx+1, housecnt):
        makecomb(n+1, i, lst+[chickenlst[i]])
makecomb(0,-1,[])
print(answer)