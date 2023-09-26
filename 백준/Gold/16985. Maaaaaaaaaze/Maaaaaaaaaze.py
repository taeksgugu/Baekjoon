'''
시간복잡도 계산
-> 5!(판 순서 정하기) * 2^10(각 판별 회전 정하기) * 5^3(BFS) = 약 10^7...?

'''
import sys
from collections import deque
input = sys.stdin.readline
N = 5
original = [[list(map(int, input().split())) for _ in range(5)] for _ in range(5)]
v = [0]*5
idxlst = []
### 판을 쌓는 순서를 만드는 함수
def makeidx(n, lst): ### 각 리스트별
    if n == 5:
        idxlst.append(lst)
        return

    for i in range(5):
        if v[i] == 0:
            v[i] = 1
            makeidx(n+1, lst+[i])
            v[i] = 0
makeidx(0, [])

### 배열과 방향이 주어지면 회전 시킨 배열을 반환하는 함수
def turn(arr,d):
    if d == 0: return arr
    newarr = [[0]*5 for _ in range(5)]
    for i in range(5):
        for j in range(5):
            if d == 1: ### 90도
                newarr[i][j] = arr[N-1-j][i]
            elif d == 2: ### 180도
                newarr[i][j] = arr[N-1-i][N-1-j]
            elif d == 3: ### 270도
                newarr[i][j] = arr[j][N-1-i]
    return newarr

def bfs(cube):
    if cube[0][0][0] == 0 or cube[-1][-1][-1]==0: return False, -1 ### 애초에 시작도 못함
    visited = [[[-1]*5 for _ in range(5)] for _ in range(5)]
    ei, ej, ek = 4, 4, 4
    q = deque()
    q.append((0,0,0))
    visited[0][0][0] = 0
    while q:
        ci, cj, ck = q.popleft()
        for di, dj, dk in [(-1,0,0), (1,0,0), (0,-1,0), (0,1,0), (0,0,-1), (0,0,1)]:
            ni, nj, nk = ci+di, cj+dj, ck+dk
            if 0<=ni<5 and 0<=nj<5 and 0<=nk<5 and cube[ni][nj][nk] == 1 and visited[ni][nj][nk] == -1:
                if ni==ei and nj==ej and nk==ek: return True, visited[ci][cj][ck]+1
                visited[ni][nj][nk] = visited[ci][cj][ck] + 1
                q.append((ni,nj,nk))

    return False, -1

### 판 별 회전을 어떻게 시킬지 정하는 함수 및 정해진 cube모양으로 bfs실행하는 함수
answer = 1e9
def maketurn(n, lst):
    global answer
    if answer == 12: return
    if n == 5:
        cnt = 1e9
        for ll in idxlst: ### 판 쌓는 순서 가져오기
            cube = [turn(original[ll[x]], lst[x]) for x in range(5)]
            can, dist = bfs(cube)
            if can: cnt = min(cnt, dist)
            else: continue
            if cnt == 12: break
        answer = min(answer, cnt)
        # print(lst)
        return

    for i in range(4):
        maketurn(n+1, lst+[i])
maketurn(0,[])

if answer == 1e9: print(-1)
else: print(answer)