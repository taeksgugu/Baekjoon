### 검은 블록 -1 무지개 0 일반은 1~M
### 인접 칸은 상하좌우
### 그룹은 1개 이상 일반 블록 (같은 색) & 검정 미포함 & 무지개 상관 x
### 그룹 기준 블록은 행, 열 작은 순 (무지개 X)
import sys
from collections import deque
input = sys.stdin.readline
### 입력받기 & 필요변수 선언
N, M = map(int, input().split()) ### 격자 한변 크기 & 색상 개수
arr = [list(map(int, input().split())) for _ in range(N)] ### 블록 배열
score = 0 ### 획득한 점수

### 중력 작용 함수 생성
def gravity(arr):
    arr_T = [x[::-1] for x in list(map(list, zip(*arr)))]
    ### 중력 작용
    newarr = []
    for i in range(N):
        line = arr_T[i]
        newlst = []
        for idx in range(N):
            num = line[idx]
            if num == -2: continue
            elif num == -1:
                if len(newlst) == idx:
                    newlst.append(num)
                else:
                    newlst += ([-2]*(idx-len(newlst)) + [-1])
            else:
                newlst.append(num)
        newarr.append(newlst+[-2]*(N-len(newlst)))
    finalarr = list(map(list, zip(*newarr)))[::-1]
    return finalarr

while True: ### 찾을 때까지 반복
    ### 크기가 가장 큰 블록 찾기
    ### 크기가 가장 큰 블록 그룹 & 무지개수 많은 순 & 기준 블록 행, 열 큰 순
    ### -> 오른쪽 끝에서부터 순회하면서 무지개수를 최대한 포함해서 블록 검색하면서 확인
    visited = [[0] * N for _ in range(N)]
    maxblock, maxi, maxj, maxrainbow = 1, -1, -1, 0 ### 크기 가장 큰 블록 변수
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            # print(i,j)
            if arr[i][j]>0: ### 블록 찾기의 시작은 일반 블록에서 해야함
                # print('검색',i,j)
                rainbowlst = []
                blocksize, rainbowcnt = 0, 0 ### 블록 그룹 사이즈 & 무지개수
                color = arr[i][j] ### 일반 블록색 저자
                bi, bj = i, j ### 기준 블록 좌표
                q = deque()
                q.append((i,j))
                visited[i][j] = 1
                while q:
                    ci, cj = q.popleft()
                    blocksize += 1
                    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<N and 0<=nj<N and visited[ni][nj] == 0 and (arr[ni][nj]==color or arr[ni][nj]==0): ### 범위내, 미방문, 같은 색상 or 무지개
                            visited[ni][nj] = 1
                            q.append((ni,nj))
                            if arr[ni][nj] == color: ### 같은 색상이라면 해당 그룹 기준 블록이 될 수 있는지 확인
                                bi, bj = sorted([(bi,bj), (ni,nj)])[0] ### 행 열 크기에 따라 정렬하고 앞에꺼 가져오기
                            else: ### 무지개면 그룹 내 무지개수 + 1
                                rainbowcnt += 1
                                rainbowlst.append((ni,nj))
                ### 무지개는 다시 미방문처리
                for ri, rj in rainbowlst:
                    visited[ri][rj] = 0

                ### 크기가 가장 큰 블록 갱신
                if blocksize > maxblock: ### 사이즈가 더 크다면 다 갱신
                    maxblock, maxrainbow, maxi, maxj = blocksize, rainbowcnt, bi, bj
                elif blocksize == maxblock: ### 사이즈가 같다면 기준에 따라 처리
                    maxrainbow, maxi, maxj = sorted([(maxrainbow, maxi, maxj), (rainbowcnt, bi, bj)], key=lambda x: (-x[0], -x[1], -x[2]))[0]


    ### 종료 조건
    if maxblock < 2: break ### 블록을 못 찾았을 경우,,,
    ### 가장 큰 블록 제거 및 점수 획득
    score += maxblock**2 ### 점수 처리
    dq = deque()
    dq.append((maxi, maxj))
    dvisited = [[0] * N for _ in range(N)]
    dvisited[maxi][maxj] = 1
    dcolor = arr[maxi][maxj]  ### 기준 블록 색상
    arr[maxi][maxj] = -2 ### 해당 블록 제거

    while dq:
        ci, cj = dq.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < N and dvisited[ni][nj] == 0 and (arr[ni][nj] == dcolor or arr[ni][nj] == 0): ### 범위내, 미방문, 같은 색상 or 무지개
                dvisited[ni][nj] = 1
                arr[ni][nj] = -2 ### 블록 제거
                dq.append((ni,nj))


    ### 중력 작용
    arr = gravity(arr)
    ### 디버깅

    ### 90도 반시계 회전
    arr = list(map(list, zip(*arr)))[::-1]

    ### 중력 작용
    arr = gravity(arr)

print(score)
