### 1차 시도 : 115136kb 132ms 풀이 시간 : 25분
### 2차 시도 : 114328kb 116ms 개선 시간 : 8분
###           메모리 감소를 위해 visited 배열을 생성하지 않고 arr에서 다 처리하는 방식으로 개선 (0:청소 x 빈칸 / 1: 벽 / 2:청소된 빈칸)
###           시간 축소를 위해 인접 칸 청소 여부 확인 때 break 추가
### 3차 시도 : 
###           시간 축소를 위해 arr를 int로 변경 시키지 않음

import sys
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().rstrip().split())
i,j,d = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]

dirlst = [(-1,0), (0,1), (1,0), (0,-1)] ### 0:북 1:동 2:남 3:서
turnlst = {0:3, 1:0, 2:1, 3:2} ### 시계 반대방향 반회전 딕셔너리
answer = 0 ### 청소하는 칸 개수

while True:
    if arr[i][j] == '0': ### 빈 칸이면서 아직 청소 안했을경우
        arr[i][j] = '2'
        answer += 1
    ### 인접한 칸 청소 여부 확인
    go = False
    for di, dj in dirlst:
        ni, nj = i+di, j+dj
        if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '0': ### 청소되지 않은 빈칸
            go = True
            break ### 어차피 한칸이라도 있을 경우 작동하기 때문에 시간 축소를 위한 break
    ### 청소되지 않은 빈 칸이 없는 경우
    if not go:
        di, dj = dirlst[d] ## 방향 가져오기
        back_i, back_j = i+di*(-1), j+dj*(-1) ### 후진이기 때문에 -1을 곱한다
        if 0<=back_i<N and 0<=back_j<M:
            if arr[back_i][back_j] == '1': ### 벽이라면 작동 멈춤
                break
            i, j = back_i, back_j
    ### 청소되지 않은 빈 칸이 있는 경우
    else:
        d = turnlst[d] ### 반시계 방향 회전
        di, dj = dirlst[d]
        ni, nj = i+di, j+dj  ### 바라보는 방향으로 전진할 칸
        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '0':  ### 청소되지 않은 빈칸
            i, j = ni, nj

print(answer)