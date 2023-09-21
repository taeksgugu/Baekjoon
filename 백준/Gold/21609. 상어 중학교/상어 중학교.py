# 시도	결과          메모리     시간      원인 및 개선 사항
# 1차	런타임 에러                       들여쓰기 실수로 인해 NameError 발생
# 2차	맞았습니다!!   118140    292      들여쓰기 수정
# 3차   IndexError                      그룹 찾을 때마다 갱신하는게 빠른지, 저장해놓고 결정하는게 빠른지 시간 비교인데 IndexError 발생
### 초기에 문제를 읽으면서 주의할 점을 정리했음
### 그리고 이전에 서용님 조언에 따라서 종이 뿐만 아니라 주석으로 먼저 주의할 점을 적어놓음
### 테케 2번을 바로 통과못했는데 그 이유는 무지개 방문처리 후 다른 그룹에서 방문할 수 있다는걸 생각 못함
### 해당 부분 rainbowlst로 처리하고 해결
### 시간이 많이 오래 걸린 부분이 중력 작용 부분, 검정색 블록이 움직이지 않는걸 처리하는데 깔끔하게 하고 싶단 생각 때문에 오래걸림
### 처음에는 중력, 회전, 중력을 같이 구현하는 함수를 만드려고 했으나, 단계별 확인을 위해서 그렇게 하지 않음

import sys
from collections import deque
input = sys.stdin.readline
### 입력받기 & 필요변수 선언
N, M = map(int, input().split()) ### 격자 한변 크기 & 색상 개수
arr = [list(map(int, input().split())) for _ in range(N)] ### 블록 배열 (검은 블록 -1 무지개 0 일반은 1~M)
score = 0 ### 획득한 점수

### 중력 작용 함수 생성
def gravity(arr):
    newarr = []
    for line in [x[::-1] for x in list(map(list, zip(*arr)))]:
        newlst = []
        for idx in range(N):
            num = line[idx]
            if num == -2: continue
            elif num == -1:
                if len(newlst) == idx:
                    newlst.append(num)
                else: newlst += ([-2]*(idx-len(newlst)) + [-1])
            else: newlst.append(num)
        newarr.append(newlst+[-2]*(N-len(newlst)))
    return list(map(list, zip(*newarr)))[::-1]

while True: ### 찾을 때까지 반복
    ### 크기가 가장 큰 블록 찾기
    ### 크기가 가장 큰 블록 그룹 & 무지개수 많은 순 & 기준 블록 행, 열 큰 순
    ### -> 오른쪽 끝에서부터 순회하면서 무지개수를 최대한 포함해서 블록 검색하면서 확인
    ### 인접 칸은 상하좌우
    visited = [[0] * N for _ in range(N)]
    ### 그룹은 1개 이상 일반 블록 (같은 색) & 검정 미포함 & 무지개 상관 x 그래서 maxblock은 1로 지정
    maxblock, maxi, maxj, maxrainbow = 1, -1, -1, 0 ### 크기 가장 큰 블록 변수
    grouplst = []
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if arr[i][j]>0: ### 블록 찾기의 시작은 일반 블록에서 해야함
                rainbowlst = [] ### 무지개는 추후 미방문 처리를 위해 리스트 저장
                blocksize, rainbowcnt, color = 0, 0, arr[i][j] ### 블록 그룹 사이즈 & 무지개수 & 일반 블록 색상
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
                                ### 그룹 기준 블록은 행, 열 작은 순 (무지개 X)
                                bi, bj = sorted([(bi,bj), (ni,nj)])[0] ### 행 열 크기에 따라 정렬하고 앞에꺼 가져오기
                            else: ### 무지개면 그룹 내 무지개수 + 1
                                rainbowcnt += 1
                                rainbowlst.append((ni,nj))
                ### 무지개는 다시 미방문처리
                for ri, rj in rainbowlst:
                    visited[ri][rj] = 0

                # ### 크기가 가장 큰 블록 갱신
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
    ### 90도 반시계 회전
    arr = list(map(list, zip(*arr)))[::-1]
    ### 중력 작용
    arr = gravity(arr)

print(score)
