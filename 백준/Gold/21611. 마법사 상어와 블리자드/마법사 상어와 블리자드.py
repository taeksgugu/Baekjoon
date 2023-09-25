import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
orderlst = [list(map(int,input().split())) for _ in range(M)]
dirlst = [(0,0), (-1,0), (1,0), (0,-1), (0,1)]
balllst = deque()
idxarr = [[-1] * N for _ in range(N)]  ### 구슬 인덱스 배열

### 구슬 리스트 만들기 및 배열 위치별 구슬 인덱스 지정
def cal():
    idxarr[N//2][N//2-1] = 0 ### start 0으로 설정
    balllst.append(arr[N//2][N//2-1]) ### 구슬 리스트 추가
    idx, k = 1, 2
    i, j = N//2+1, N//2-1
    while idx < N**2-1:
        if k%2 == 0:
            for _ in range(1,k+1):
                balllst.append(arr[i][j])
                idxarr[i][j] = idx
                i, j = i, j+1
                idx += 1
                if idx >= N**2-1: return
            for _ in range(1,k+1):
                balllst.append(arr[i][j])
                idxarr[i][j] = idx
                i, j = i - 1, j
                idx += 1
                if idx >= N ** 2 - 1: return
            k += 1
        else:
            for _ in range(1,k+1):
                balllst.append(arr[i][j])
                idxarr[i][j] = idx
                i, j = i, j - 1
                idx += 1
                if idx >= N ** 2 - 1: return
            for _ in range(1,k+1):
                balllst.append(arr[i][j])
                idxarr[i][j] = idx
                i, j = i+1, j
                idx += 1
                if idx >= N ** 2 - 1: return
            if idx >= N ** 2 - 1: return
            k += 1
cal()
### 디버깅
# for l in idxarr:
#     print('\t'.join([str(x) for x in l]))
# print()
# print(len(balllst), balllst)

totalcnt = [0, 0, 0, 0] ### 폭발하는 구슬 번호별 갯수

for ordernum in range(M):
    ### 상어가 구슬 파괴
    dirnum, snum = orderlst[ordernum]
    si, sj = N//2, N//2
    di, dj = dirlst[dirnum]
    for sn in range(1, snum+1): ### si의 범위가 (N-1)//2 여서 바깥으로 나갈 걱정 x
        ni, nj = si+di*sn, sj+dj*sn
        balllst[idxarr[ni][nj]] = 0 ### 해당 인덱스 위치 구슬 부시기

    ### 디버깅
    # print('구슬 파괴 후')
    # print(balllst)

    ### 구슬 빈칸 이동
    for _ in range(len(balllst)):
        ball = balllst.popleft()
        if ball != 0: balllst.append(ball) ### 빈칸이 아니라면
        else: continue ### 걍 보내버리기
    balllst += [0]*(N**2-1-len(balllst))

    ### 디버깅
    # print('구슬 이동 후')
    # print(balllst)

    ### 구슬 폭발 단계
    while True:
        flag = False
        before = balllst.popleft() ### 맨 처음꺼
        lst = [before]
        for _ in range(len(balllst)):
            ball = balllst.popleft()
            if ball == before:
                lst.append(before)
            else: ### 다르면
                if len(lst) >= 4: ### 이전꺼가 4개 이상이면
                    flag = True
                    totalcnt[before] += len(lst) ### 폭발 개수 정산
                else: ### 4개 이하면 그대로 넣기
                    balllst += lst
                before, lst = ball, [ball]
        ### 마지막 처리
        if len(lst)<4: balllst += lst
        else:
            totalcnt[before] += len(lst)

        ### 디버깅
        # print('구슬 폭발 단계 확인')
        # print(flag, balllst)
        if not flag: ### 한번도 폭발 안했다면
            break
        if not balllst: ### 다 없어졌다면?
            break

    ### 디버깅
    # print('구슬 폭발 후')
    # print(balllst)

    if not balllst: break ### 아예 구슬이 없다면?

    ### 구슬 변화 단계
    newball = []
    before = balllst.popleft()  ### 맨 처음꺼
    ballcnt = 1
    for _ in range(len(balllst)):
        ball = balllst.popleft()
        if before == ball:
            ballcnt += 1
        else:
            newball.append(ballcnt)
            newball.append(before)
            before, ballcnt = ball, 1
    ### 마지막 처리
    newball.append(ballcnt)
    newball.append(before)
    if len(newball) <= N**2-1:
        balllst = deque(newball + [0]*(N**2-1-len(newball)))
    else: ### 칸수보다 많으면
        balllst = deque(newball[:N**2-1])

    ### 디버깅
    # print('구슬 변화 후')
    # print(len(balllst))
    # print(balllst)

# print(totalcnt)
print(sum([x*totalcnt[x] for x in range(4)]))