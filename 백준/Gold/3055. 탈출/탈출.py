import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
R, C = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)]
def solve():
    time = 1
    visited = [[0]*C for _ in range(R)]
    water = deque()
    hedgehog = deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '*':
                water.append((i,j))
            elif arr[i][j] == 'S':
                hedgehog.append((i,j))
            elif arr[i][j] == 'D':
                beaver_i, beaver_j = i,j
    while True:
        ### 먼저 홍수부터 처리 -> 물이 지나가면 1로 처리
        for _ in range(len(water)):
            i, j = water.popleft()
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i + di, j +dj
                ### 주변이 비어있고 물이 넘친적이 없다면
                if 0<=ni<R and 0<=nj<C and arr[ni][nj] == '.' and visited[ni][nj] != 1:
                    water.append((ni,nj))
                    arr[ni][nj] = '*'
                    visited[ni][nj] = 1
        ### 고슴도치가 이제 갈곳 찾기 -> 방문한 곳은 2로 처리
        for _ in range(len(hedgehog)):
            i, j = hedgehog.popleft()
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i + di, j +dj
                ### 주변이 비어있다면
                if 0<=ni<R and 0<=nj<C:
                    if arr[ni][nj] == '.' and visited[ni][nj] == 0:
                        hedgehog.append((ni,nj))
                        visited[ni][nj] = 2
                    elif arr[ni][nj] == 'D':
                        return time
        if not hedgehog:
            return 'KAKTUS'
        time += 1
print(solve())