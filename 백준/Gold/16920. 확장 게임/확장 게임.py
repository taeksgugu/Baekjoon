import sys
from collections import deque
input = sys.stdin.readline

N, M, P = map(int, input().split())
castlelst = [deque() for _ in range(P + 1)]
slst = [0] + list(map(int, input().split()))
arr = [list(input().rstrip()) for _ in range(N)]
answer = [0]*(P+1)

for i in range(N):
    for j in range(M):
        if arr[i][j] != '.' and arr[i][j] != '#': ### 성곽일 때
            answer[int(arr[i][j])] += 1
            castlelst[int(arr[i][j])].append((i, j))
### 방향리스트
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]

### 전체 진행 함수
def solve():
    while True:
        flag = False
        for pnum in range(1, P+1):
            if not castlelst[pnum]: continue # 비어있다면 continue
            q = castlelst[pnum]
            sp = slst[pnum]
            for _ in range(sp): ### 주어진 sp 만큼 이동
                if not q: break
                for _ in range(len(q)):
                    ci, cj = q.popleft()
                    for di, dj in dirlst:
                        ni, nj = ci+di, cj+dj
                        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '.':
                            arr[ni][nj] = str(pnum)
                            q.append((ni,nj))
                            answer[pnum] += 1
                            flag = True
        if not flag: break

    return answer[1:]
print(*solve())