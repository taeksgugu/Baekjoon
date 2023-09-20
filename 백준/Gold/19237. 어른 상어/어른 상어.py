import sys
input = sys.stdin.readline
### 입력 받기
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
### 상어 위치 관리
sharkpos = [[] for _ in range(M + 1)]
### 냄새 관리
smellarr = [[[0, 0] for _ in range(N)] for _ in range(N)]
# 방향리스트
# dirlst = [(-1, 0), (1, 0), (0, -1), (0, 1)] ### 0:상 1:하 2:좌 3:우
#
# ### 상어 번호별 위치 확인
# for i in range(N):
#     for j in range(N):
#         if arr[i][j] != 0:
#             sharkpos[arr[i][j]].append([i, j])
# ### 상어 번호별 방향 확인
# dirdata = list(map(lambda x: int(x)-1, input().split()))
# for i in range(1, M + 1):
#     sharkpos[i].append(dirdata[i - 1])
# ### 상어 번호별 위치 우선순위
# sharkrank = {}
# for i in range(1, M + 1):
#     sharkrank[i] = [0]
#     for j in range(1, 5):
#         sharkrank[i].append(list(map(lambda x: int(x)-1, input().split())))
dirlst = [[], (-1, 0), (1, 0), (0, -1), (0, 1)] ### 0:상 1:하 2:좌 3:우

### 상어 번호별 위치 확인 및 냄새 정리
for i in range(N):
    for j in range(N):
        if arr[i][j] != 0:
            sharkpos[arr[i][j]].append([i, j])
            smellarr[i][j] = [arr[i][j], K]
### 상어 번호별 방향 확인
dirdata = list(map(int, input().split()))
for i in range(1, M + 1):
    sharkpos[i].append(dirdata[i - 1])
### 상어 번호별 위치 우선순위
sharkrank = {}
for i in range(1, M + 1):
    sharkrank[i] = [0]
    for j in range(1, 5):
        sharkrank[i].append(list(map(int, input().split())))

# 인접한 칸 확인 함수
def checknear(smellarr, num):
    si, sj = sharkpos[num][0]
    sdir = sharkpos[num][1]
    for dirnum in sharkrank[num][sdir]:
        di, dj = dirlst[dirnum]
        ni, nj = si + di, sj + dj
        if 0<=ni<N and 0<=nj<N:
            if smellarr[ni][nj][0] == 0:
                return [ni,nj, dirnum]
    return False # 빈 곳이 없는 경우
# 내 냄새가 있는 방향 확인
def checksmell(smellarr, num):
    si, sj = sharkpos[num][0]
    sdir = sharkpos[num][1]
    for dirnum in sharkrank[num][sdir]:
        di, dj = dirlst[dirnum]
        ni, nj = si+di, sj+dj
        if 0<=ni<N and 0<=nj<N:
            if smellarr[ni][nj][0] == num:
                return [ni,nj, dirnum]

# 살아있는 상어의 수
remaincnt = M
# 이동 횟수
ans = 0
while remaincnt > 1 and ans < 1001:
    # 상어 움직임
    for i in range(1, M + 1):
        # 현재 상어가 죽어있다면 건너뜀
        if sharkpos[i][0] == -1:
            continue

        near = checknear(smellarr, i)

        # 인접한 칸 비어있는지 확인
        if near:
            newi, newj, newdir = near

        else: ### 만약 인접한 곳에 빈 칸이 없다면 우선순위에 따른 움직임
            smell_move = checksmell(smellarr, i)
            newi, newj, newdir = smell_move[0], smell_move[1], smell_move[2]
        sharkpos[i][0][0], sharkpos[i][0][1] = newi, newj
        sharkpos[i][1] = newdir

    # 죽은 상어 있는지 확인 후 업데이트
    deadcnt = 0
    for i in range(1, M):
        if sharkpos[i][0] == -1: continue  ### 죽은 상어
        for j in range(i + 1, M + 1): ### 해당 상어 번호 뒤로 확인
            if sharkpos[j][0] == -1:
                continue

            if sharkpos[i][0] == sharkpos[j][0]: ### 두 마리의 상어가 위치가 같다면?
                sharkpos[max(i, j)][0] = -1 ### 큰 번호 죽음
                deadcnt += 1 ### 죽은 상어수 + 1

    remaincnt -= deadcnt

    # 냄새 처리
    for i in range(N):
        for j in range(N):
            if smellarr[i][j][0] != 0:
                smellarr[i][j][1] -= 1
            if smellarr[i][j][1] == 0: ### 0이면 상어 흔적도 없애기
                smellarr[i][j][0] = 0

    # 상어 냄새 남기기
    for i in range(1, M+1):
        if sharkpos[i][0] != -1: ### 살아있다면
            nsi, nsj = sharkpos[i][0]
            smellarr[nsi][nsj] = [i, K]
    ans += 1

if ans > 1000:
    print(-1)
else:
    print(ans)