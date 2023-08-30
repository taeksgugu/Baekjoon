import sys
from collections import deque
input = sys.stdin.readline
arr = []
N, M = map(int, input().rstrip().split())
### 연구실 입력 및 바이러스 위치 리스트 생성
viruslst = []
emptycnt = 0
for i in range(N):
    lst = list(map(int, input().rstrip().split()))
    for j in range(N):
        if lst[j] == 2:
            viruslst.append((i,j))
        elif lst[j] == 0:
            emptycnt += 1
    arr.append(lst)
### M개의 바이러스가 퍼지는 속도 구하기
def bfs(active):
    delcnt = emptycnt
    q = deque(active)
    visited = [['-']*N for _ in range(N)]
    maxnum = 0
    for i, j in q:
        visited[i][j] = 0
    while q:
        i, j = q.popleft()
        time = visited[i][j]
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] != 1 and (visited[ni][nj] == '-'):
                if arr[ni][nj] == 0:
                    maxnum = time+1
                    visited[ni][nj] = time + 1
                    delcnt -= 1
                    q.append((ni,nj))
                elif arr[ni][nj] == 2:
                    visited[ni][nj] = time + 1
                    q.append((ni,nj))
    if delcnt == 0:
        return maxnum
    return -1
### 조합 수 만들어서 진행
def comb(n, lst, idx):
    global zero, answer
    if n==M:
        ans = bfs(lst)
        if ans != -1:
            zero = True
            answer = min(answer, ans)
        return
    for i in range(idx+1, len(viruslst)):
        comb(n+1, lst+[viruslst[i]], i)
answerlst = []
zero = False
answer = N**2
comb(0,[],-1)
if not zero:
    print(-1)
else:
    print(answer)