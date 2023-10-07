import sys
from collections import deque
input = sys.stdin.readline

### 입력 받기
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

emptylst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0: emptylst.append((i,j))
def findgroup():
    grouplst = []
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2 and visited[i][j] == 0:
                cnt = 1
                outside = set()
                q = deque()
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<N and 0<=nj<M and visited[ni][nj]==0:
                            if arr[ni][nj] == 2:
                                visited[ni][nj] = 1
                                q.append((ni,nj))
                                cnt += 1
                            else: outside.add((ni,nj))
                grouplst.append((cnt, outside))
    return grouplst

grouplst = findgroup()
# print(grouplst)
def check():
    can, maxcnt = False, 0
    for groupcnt, groupout in grouplst:
        flag = False
        for gi, gj in groupout:
            if arr[gi][gj] == 1: continue
            else:
                flag = True
                break
        if not flag:
            can = True
            maxcnt += groupcnt

    return can, maxcnt

answer = 0
def baduk(n, idx):
    global answer
    if n == 2:
        can, arrcnt = check()
        if can: answer = max(answer, arrcnt)
        # for l in arr:
        #     print(*l)
        # print(arrcnt)
        return

    for i in range(idx+1, len(emptylst)):
        bi, bj = emptylst[i]
        arr[bi][bj] = 1
        baduk(n+1, i)
        arr[bi][bj] = 0

baduk(0,-1)
print(answer)