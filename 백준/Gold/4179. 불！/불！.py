import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
R, C = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)]
def solve():
    time = 1
    visited = [[0]*C for _ in range(R)]
    fire = deque()
    Jihoon = deque()
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'F':
                fire.append((i,j))
            elif arr[i][j] == 'J':
                Jihoon.append((i,j))
    while True:
        ### 먼저 불부터 처리 -> 불이 지나가면 1로 처리
        for _ in range(len(fire)):
            i, j = fire.popleft()
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i + di, j +dj
                ### 주변이 비어있고 불이 아직 안 번졌다면
                if 0<=ni<R and 0<=nj<C and arr[ni][nj] == '.' and visited[ni][nj] != 1:
                    fire.append((ni,nj))
                    arr[ni][nj] = 'F'
                    visited[ni][nj] = 1
        ### 지훈이가 이제 갈곳 찾기 -> 방문한 곳은 2로 처리
        for _ in range(len(Jihoon)):
            i, j = Jihoon.popleft()
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i + di, j +dj
                if ni == R or nj == C or ni == -1 or nj == -1:
                    return time
                ### 주변이 비어있다면
                if 0<=ni<R and 0<=nj<C and arr[ni][nj] == '.' and visited[ni][nj] == 0:
                    Jihoon.append((ni,nj))
                    visited[ni][nj] = 2
        if not Jihoon:
            return 'IMPOSSIBLE'
        time += 1
print(solve())