### 초기 풀이 과정: 딱 봐도 너무 귀찮고 복잡한 구현이라는걸 깨달음
###             단계별로 해결 온풍기 바람 -> 조절-> 온도 -1
### 1차 시도 : 시간초과 풀이 시간 : 1시간 20분

### 2차 시도 : 시간 초과 수정 시간 : 15분
###          온풍기가 바람을 보내는 과정을 좀 더 간단하게 만듦
### 3차 시도 :
###          반복문 돌 때마다 계산하게 만들지 말고 온풍기 바람이 가는 곳을 리스트로 만들어서 진행시키기!
import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
R, C, K = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(R)]
W = int(input())
walldata = [list(map(int, input().split())) for _ in range(W)]
### 방향리스트
dirlst = {'R':(0,1), 'L':(0,-1), 'U':(-1,0), 'D':(1,0)}
wallchklst = {'R': [[(-1,0), (-1,1)], [(0,1)], [(1,0), (1,1)]],
              'L':[[(-1,0), (-1,-1)], [(0,-1)], [(1,0), (1,-1)]],
              'U': [[(0,-1), (-1,-1)], [(-1,0)], [(0,1), (-1,1)]],
              'D':[[(0,-1), (1,-1)], [(1,0)], [(0,1), (1,1)]]}

### 온풍기 리스트 만들기 & 온도 조사 칸 리스트 만들기
warmlst, chklst = [], []
for i in range(R):
    for j in range(C):
        if arr[i][j] == 1: ### 1: 방향이 오른쪽인 온풍기가 있음
            warmlst.append((i,j,'R'))
        elif arr[i][j] == 2: ### 2: 방향이 왼쪽인 온풍기가 있음
            warmlst.append((i, j, 'L'))
        elif arr[i][j] == 3: ### 3: 방향이 위인 온풍기가 있음
            warmlst.append((i, j, 'U'))
        elif arr[i][j] == 4:  ### 4: 방향이 아래인 온풍기가 있음
            warmlst.append((i, j, 'D'))
        elif arr[i][j] == 5: ### 5: 온도를 조사해야 하는 칸
            chklst.append((i,j))
arr = [[0]*C for _ in range(R)]
### 벽 리스트 만들기
walllst = []
for x, y, t in walldata:
    if t == 0:
        walllst.append((x-1,y-1,x-2,y-1))
        walllst.append((x-2,y-1,x-1,y-1))
    else:
        walllst.append((x-1,y-1,x-1,y))
        walllst.append((x-1,y,x-1,y-1))
# print(walllst)
### 모든 온풍기 바람 나오는 함수
def warmwind(warmlst):
    winddic = {}
    for wi,wj,wdir in warmlst:
        # print(wi,wj,wdir)
        visited = [[0]*C for _ in range(R)]
        ni, nj = wi+dirlst[wdir][0], wj+dirlst[wdir][1] ### 첫번째 칸 조건:
        q = deque()           ### 온풍기가 있는 칸과 바람이 나오는 방향에 있는 칸 사이에는 벽이 없다.
        q.append((ni, nj,5))   ### 온풍기의 바람이 나오는 방향에 있는 칸은 항상 존재한다.
        visited[ni][nj] = 1
        try: winddic[(ni,nj)] += 5
        except: winddic[(ni,nj)] = 5
        # arr[ni][nj] += 5
        while q:
            ci, cj, temp = q.popleft()
            for golst in wallchklst[wdir]:
                bi, bj = ci, cj  ### 벽 막혔는지 확인하기 위한 변수 (이전 위치)
                for di, dj in golst:
                    nni, nnj = ci+di, cj+dj
                    if nni<0 or nni>=R or nnj<0 or nnj>=C: break
                    if (bi,bj,nni,nnj) in walllst: break
                    bi, bj = nni, nnj
                else:
                    if temp>1 and visited[nni][nnj] == 0:
                        visited[nni][nnj] = 1
                        try: winddic[(nni, nnj)] += temp-1
                        except: winddic[(nni, nnj)] = temp-1
                        # arr[nni][nnj] += temp-1
                        if temp-1>1: ### 굳이 추가해서 시간초과할 필요 X
                            q.append((nni,nnj,temp-1))
    return winddic
winddic = warmwind(warmlst)
### 온도 조절 함수
def control():
    newarr = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            A = arr[i][j]
            for di, dj in [(0,1), (1,0)]:
                ni, nj = i+di, j+dj
                if (i,j,ni,nj) not in walllst and 0<=ni<R and 0<=nj<C:
                    B = arr[ni][nj]
                    value = abs(A-B)//4
                    if A>=B:
                        newarr[i][j] -= value
                        newarr[ni][nj] += value
                    else:
                        newarr[i][j] += value
                        newarr[ni][nj] -= value

    for i in range(R):
        for j in range(C):
            arr[i][j] += newarr[i][j]

chocolatecnt = 0 ### 구사과가 먹는 초콜릿 개수
# print(walllst)
while True:
    ### 모든 온풍기 바람이 나옴
    for ij, val in winddic.items():
        # print(ij)
        arr[ij[0]][ij[1]] += val
    # warmwind(warmlst)

    ### 온도 조절
    control()
    ### 가장 바깥족 칸 온도 -1
    for i in range(R):
        for j in range(C):
            if i == 0 or i == R-1 or j == 0 or j == C-1: ### 1행 or R행 or 1열 or C열
                if arr[i][j] > 0: arr[i][j] -= 1
    ### 초콜릿 먹기
    chocolatecnt += 1

    if chocolatecnt > 100: ### 초콜릿 개수 100 넘으면
        print(101)
        break
    ###조사해야 하는 칸 온도 조사
    for chki, chkj in chklst:
        if arr[chki][chkj] < K: break
    else:
        # for l in arr:
        #     print(*l)
        # print()
        print(chocolatecnt)
        break