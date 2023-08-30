import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = [input().rstrip() for _ in range(N)]
visited = [[0]*N for _ in range(N)]
answerlst = []

def dfs(i,j):
    global length
    queue = [(i,j)]
    while queue:
        node_i, node_j = queue.pop(0)
        if visited[node_i][node_j] == 0:
            visited[node_i][node_j] = length
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = node_i+di, node_j+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj] == '1' and visited[ni][nj] == 0:
                    length+=1
                    dfs(ni,nj)
for i in range(N):
    for j in range(N):
        if arr[i][j] == '1' and visited[i][j] == 0:
            length = 1
            dfs(i,j)
            answerlst.append(length)
answerlst.sort()
print(len(answerlst))
for ans in answerlst:
    print(ans)