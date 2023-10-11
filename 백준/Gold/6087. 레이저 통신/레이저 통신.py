import sys
from collections import deque
input = sys.stdin.readline

W, H = map(int, input().split())
arr = [list(input()) for _ in range(H)]
lst = []
for i in range(H):
    for j in range(W):
        if arr[i][j] == 'C': lst.append((i,j))
si, sj = lst[0]
ei, ej = lst[1]
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]
visited = [[-1]*W for _ in range(H)]
def solve():
    q = deque()
    q.append((si,sj))
    cnt = 0
    visited[si][sj] = 0
    while q:
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in dirlst:
                k = 1
                while True:
                    ni, nj = ci+di*k, cj+dj*k
                    if ni<0 or ni>=H or nj<0 or nj>=W or arr[ni][nj] == '*': break
                    if 0<=ni<H and 0<=nj<W and visited[ni][nj] == -1:
                        visited[ni][nj] = cnt
                        q.append((ni,nj))
                        if (ni,nj) == (ei,ej):
                            return cnt
                    k += 1

        cnt += 1

print(solve())