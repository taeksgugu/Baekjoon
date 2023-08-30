import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N, M = map(int, input().rstrip().split())
arr = [list(map(lambda x: x if x == '+' else '@', list(input().rstrip()))) for _ in range(N)]
### 미로 두 구멍 찾기
holelst = []
for i in range(N):
    for j in range(M):
        if (i==0 or j==0 or j==M-1 or i==N-1) and arr[i][j] == '@':
            holelst.append((i,j))
start_i, start_j = holelst[0]
end_i, end_j = holelst[1]
arr[start_i][start_j] = '.'
go = True
def dfs(i, j):
    global go
    ### 미로 하나로 경로 찾기
    if not go:
        return
    if i == end_i and j == end_j:
        go = False
        for l in arr:
            print(''.join(l))
        return
    for di, dj in [(0,1),(0,-1), (1,0),(-1,0)]:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '@':
            arr[ni][nj] = '.'
            dfs(ni,nj)
            arr[ni][nj] = '@'
    return
dfs(start_i, start_j)