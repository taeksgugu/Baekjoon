import sys
input = sys.stdin.readline
R, C, K = map(int,input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)][::-1]
visited = [[0]*C for _ in range(R)]
visited[0][0] = 1
answer = 0
def dfs(i,j,k):
    global answer
    if i == R-1 and j == C-1:
        if k == K:
            answer += 1
        return
    for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
        ni, nj = i+di, j+dj
        if 0<=ni<R and 0<=nj<C and arr[ni][nj] == '.' and visited[ni][nj] == 0:
            visited[ni][nj] = 1
            dfs(ni,nj, k+1)
            visited[ni][nj] = 0
dfs(0,0,1)
print(answer)