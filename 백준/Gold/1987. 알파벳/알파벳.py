import sys
input = sys.stdin.readline
R, C = map(int, input().rstrip().split())
visited = [0]*26
arr = [input().rstrip() for _ in range(R)]
answer = 0
visited[ord(arr[0][0])-65] = 1
def dfs(i,j, cnt):
    global answer
    # print(i,j, cnt)
    answer = max(answer, cnt)
    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
        ni, nj = i+di, j+dj
        if 0<=ni<R and 0<=nj<C and visited[ord(arr[ni][nj])-65] == 0:
            visited[ord(arr[ni][nj]) - 65] = 1
            dfs(ni,nj, cnt+1)
            visited[ord(arr[ni][nj]) - 65] = 0
dfs(0,0,1)
print(answer)