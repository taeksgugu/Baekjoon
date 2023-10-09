import sys
from collections import deque
input = sys.stdin.readline

H, W = map(int, input().split())
arr = []
for _ in range(H):
    arr.append([0 if x=='.' else int(x) for x in list(input()[:W])])

def solve():
    checklst = deque()
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 0: checklst.append((i, j))
    answer = 0
    visited = [[0]*W for _ in range(H)]
    while checklst:
        ci, cj = checklst.popleft()
        for di, dj in [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W and arr[ni][nj]>0:
                arr[ni][nj] -= 1
                if not arr[ni][nj]:
                    visited[ni][nj] = visited[ci][cj] + 1
                    answer = max(answer, visited[ni][nj])
                    checklst.append((ni,nj))
    return answer
print(solve())