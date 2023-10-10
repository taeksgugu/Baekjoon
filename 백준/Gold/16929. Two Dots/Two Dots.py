import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

visited = [[0] * M for _ in range(N)]
def check(n, ci, cj):
    global answer
    # print(n, ci, cj)
    if n>=4 and (ci, cj)==(si, sj):
        answer = True
        return
    if answer: return
    for di, dj in [(-1,0), (1,0), (0,1), (0,-1)]:
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj]==arr[si][sj] and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            check(n+1, ni, nj)
            visited[ni][nj] = 0

flag = False
for i in range(N):
    for j in range(M):
        visited = [[0]*M for _ in range(N)]
        si, sj = i, j
        answer = False
        check(1, si, sj)
        if answer:
            print('Yes')
            flag = True
            break
    if flag: break
else: print('No')