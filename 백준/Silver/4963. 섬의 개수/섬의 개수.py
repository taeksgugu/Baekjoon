import sys
from collections import deque
input = sys.stdin.readline
def bfs(a,b):
    q = deque([(a,b)])
    visited[a][b] = 1
    while q:
        i, j = q.popleft()
        for di, dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
            ni,nj = i+di, j+dj
            if 0<=ni<h and 0<=nj<w and arr[i][j] == '1' and visited[ni][nj] == 0:
                q.append((ni,nj))
                visited[ni][nj] = 1
while True:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    else:
        arr = [input().rstrip().split() for _ in range(h)]
        visited = [[0]*w for _ in range(h)]
        answer = 0
        for i in range(h):
            for j in range(w):
                if arr[i][j] == '1' and visited[i][j] == 0:
                    answer += 1
                    bfs(i,j)
        print(answer)