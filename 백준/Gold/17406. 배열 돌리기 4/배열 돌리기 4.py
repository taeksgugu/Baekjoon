import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
orderlst = [list(map(int, input().split())) for _ in range(K)]

### R, C, S가 주어질 때 진행하는 함수
def turnarr(partarr):
    R, C = len(partarr), len(partarr[0])
    newarr = [[0]*C for _ in range(R)]
    for i in range(min(R, C)//2+1):
        q = deque()
        q.extend(partarr[i][i:C-i])
        q.extend([x[C-i-1] for x in partarr[i+1:C-i-1]])
        q.extend(partarr[C-i-1][i:C-i][::-1])
        q.extend([x[i] for x in partarr[i+1:C-i-1][::-1]])
        q.rotate(1)
        for j in range(i, C-i): newarr[i][j] = q.popleft()
        for j in range(i+1, R-i-1): newarr[j][C-i-1] = q.popleft()
        for j in range(C-i-1, i-1, -1): newarr[R-i-1][j] = q.popleft()
        for j in range(R-i-2, i, -1): newarr[j][i] = q.popleft()
    return newarr

### 회전 명령 내렸을 때 돌려주는 함수
def calarr(lst, arr):
    answer = [e[:] for e in arr]
    for cr, cc, cs in lst:
        partarr = [x[cc-1-cs:cc+cs] for x in answer[cr-1-cs:cr+cs]]
        newarr = turnarr(partarr)
        for i in range(2*cs+1):
            for j in range(2*cs+1):
                answer[cr-1-cs+i][cc-1-cs+j] = newarr[i][j]
        ### 디버깅
        # for l in answer:
        #     print(*l)
        # print()
    return min(map(sum, answer))

v = [0]*K
answer = 1e9
def solve(n, lst):
    global answer
    if n == K:
        val = calarr(lst, arr)
        # print(lst, val)
        answer =min(answer, val)
        return

    for i in range(K):
        if v[i] == 0:
            v[i] = 1
            solve(n+1, lst+[orderlst[i]])
            v[i] = 0

solve(0,[])
print(answer)