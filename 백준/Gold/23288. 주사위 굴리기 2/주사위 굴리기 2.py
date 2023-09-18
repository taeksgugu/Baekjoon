import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
N, M, K = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

### 디버깅용
dirq = {0:'동', 1:'남', 2:'서', 3:'북'}
### 주사위 이동 관련 변수 세팅
dice = [2,4,1,3,5,6] ### 주사위 초기 형태
dirlst = [(0,1), (1,0), (0,-1), (-1,0)] ### 동:0 남:1 서:2 북:3
changedir = {0:2, 2:0, 1:3, 3:1}
def change(dice, dir): ### 주사위 회전시키는 함수(실수 가능성 있음)
    if dir == 0: ### 동쪽으로
        lst = [0,5,1,2,4,3]
        return [dice[i] for i in lst]
    elif dir == 1: ### 남쪽으로
        lst = [5,1,0,3,2,4]
        return [dice[i] for i in lst]
    elif dir == 2: ### 서쪽으로
        lst = [0,2,3,5,4,1]
        return [dice[i] for i in lst]
    else:### 북쪽으로
        lst = [2,1,4,3,5,0]
        return [dice[i] for i in lst]


totalscore = 0 ### 최종 점수
movecnt = 0 ### 이동 횟수
si, sj, sdir = 0, 0, 0 ### 시작 좌표 & 첫 방향(동쪽)

while movecnt<K:
    movecnt += 1
    di, dj = dirlst[sdir]
    ni, nj = si+di, sj+dj
    # print(ni,nj,sdir)
    if ni<0 or ni>=N or nj<0 or nj>=M: ### 벗어날 경우 즉, 칸이 없음
        sdir = changedir[sdir] ### 반대 방향으로 change
        di, dj = dirlst[sdir]
        ni, nj = si+di, sj+dj
    ### 이동 후 도착한 칸 점수 계산 (N은 2 이상이기 때문에 방향 전환 후 범위 내인지 확인 필요 X)
    si, sj = ni, nj
    # print(ni,nj)
    dice = change(dice, sdir) ### 최종 방향으로 주사위 회전
    A, B = dice[-1], arr[ni][nj] ### 점수 계산을 위한 A, B 가져오기
    ### 점수 계산
    visited = [[0]*M for _ in range(N)]
    C = 1
    visited[ni][nj] = 1
    q = deque()
    q.append((ni,nj))
    # print('점수 계산')
    while q:
        ki, kj = q.popleft()
        # print(ki,kj)
        for ci, cj in dirlst:
            scorei, scorej = ki + ci, kj + cj
            if 0 <= scorei < N and 0 <= scorej < M and arr[scorei][scorej] == B and visited[scorei][scorej] == 0:
                visited[scorei][scorej] = 1
                C += 1
                q.append((scorei, scorej))
    # print(C)
    totalscore += B*C
    ### 방향 전환 확인
    if A>B: sdir = (sdir+1)%4 ### 시계 방향 90도
    elif A<B: sdir = (sdir-1)%4 ### 반시계 방향 90도
    # print(dice, '위치', ni+1,nj+1, '방향', dirq[sdir], '점수', totalscore)
print(totalscore)
