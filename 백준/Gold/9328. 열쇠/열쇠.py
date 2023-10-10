from collections import deque
import sys
input = sys.stdin.readline

### 방향 리스트
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]

### 열쇠찾아 문서 찾기 -> 열쇠 찾으면 리셋해서 돌기
def solve():
    q = deque()
    visited = [[0]*(W+2) for _ in range(H+2)]
    q.append((0,0))
    visited[0][0] = 1
    answer = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in dirlst:
            ni, nj = ci+di, cj+dj
            if 0<=ni<H+2 and 0<=nj<W+2 and visited[ni][nj] == 0:
                if arr[ni][nj] == '.':
                    visited[ni][nj] = 1
                    q.append((ni,nj))
                elif arr[ni][nj].islower():
                    keylst.append(arr[ni][nj].upper())
                    q = deque()
                    visited = [[0]*(W+2) for _ in range(H+2)]
                    arr[ni][nj] = '.'
                    q.append((ni,nj))
                elif arr[ni][nj].isupper():
                    if arr[ni][nj] in keylst:
                        visited[ni][nj] = 1
                        arr[ni][nj] = '.'
                        q.append((ni,nj))
                elif arr[ni][nj] == '$':
                    visited[ni][nj] = 1
                    answer += 1
                    arr[ni][nj] = '.'
                    q.append((ni,nj))
    return answer

T = int(input())
for _ in range(T):
    H, W = map(int, input().split())
    arr = [['.']*(W+2)] + [['.'] + list(input()[:W]) + ['.'] for _ in range(H)] + [['.']*(W+2)]
    keylst = [x.upper() for x in list(input()) if x != '\n']
    for i in range(H+2):
        for j in range(W+2):
            if arr[i][j].upper() in keylst: arr[i][j] = '.'
    print(solve())