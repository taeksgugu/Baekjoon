import sys
from collections import deque
input = sys.stdin.readline

### 입력받기
N, M = map(int, input().split())
arr = [list(map(int, list(input()[:M]))) for _ in range(N)]

viruslst = [deque() for _ in range(6)]
for i in range(N):
    for j in range(M):
        if arr[i][j] != 0:
            viruslst[arr[i][j]].append((i, j))

def check():
    cnt = 0
    visited = [[0]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and visited[i][j]==0:
                cnt += 1
                if cnt>=2: return False
                visited[i][j] = 1
                q = deque()
                q.append((i,j))
                while q:
                    ci, cj = q.popleft()
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<N and 0<=nj<M and arr[ni][nj] != 0 and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            q.append((ni,nj))
    return True


def solve():
    time = 0
    while True:
        ### 곰팡이 덩어리 수 확인
        if check(): return time
        ### 곰팡이 번식 시작
        for num in range(5,0,-1):
            for _ in range(len(viruslst[num])):
                ci, cj = viruslst[num].popleft()
                mini, maxi = max(0,ci-num), min(N,ci+num+1)
                minj, maxj = max(0,cj-num), min(M,cj+num+1)
                for ki in range(mini, maxi):
                    for kj in range(minj, maxj):
                        if arr[ki][kj] != num:
                            arr[ki][kj] = num
                            viruslst[num].append((ki,kj))
        time += 1
print(solve())