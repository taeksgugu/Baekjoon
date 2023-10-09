import sys
input = sys.stdin.readline

R1, C1 = map(int, input().split())
R2, C2 = map(int, input().split())
N, M = 10, 9

golst = [[(-1,0), (-1,-1), (-1,-1)], [(-1,0), (-1,1), (-1,1)], [(1,0), (1,-1), (1,-1)],
         [(1,0), (1,1), (1,1)], [(0,1), (-1,1), (-1,1)], [(0,1), (1,1), (1,1)],
         [(0,-1), (-1,-1), (-1,-1)], [(0,-1), (1,-1), (1,-1)]]

visited =[[0]*M for _ in range(N)]
visited[R1][C1] = 1
answer = 1e9
def solve(n, i, j):
    global answer
    if i==R2 and j==C2:
        answer = min(answer, n)
        return

    if n>=answer: return

    for godir in golst:
        ci, cj = i, j
        for idx in range(3):
            di, dj = godir[idx]
            ci, cj = ci+di, cj+dj
            if ci<0 or ci>=N or cj<0 or cj>=M: break
            if idx!=2 and (ci,cj) == (R2,C2): break
        else:
            if visited[ci][cj] == 0:
                visited[ci][cj] = 1
                solve(n+1, ci, cj)
                visited[ci][cj] = 0

solve(0,R1,C1)
if answer == 1e9: print(-1)
else: print(answer)