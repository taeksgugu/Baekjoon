### 1차 시도 : IndexError  풀이 시간 1시간 50분
###          방향 전환에 있어서 if문 입력 실수
import sys
input = sys.stdin.readline
### 입력 받기
R, C, M = map(int, input().rstrip().split())
sharkmap = [[[] for _ in range(C)] for _ in range(R)]
for _ in range(M):
    r,c,s,d,z = map(int, input().rstrip().split())
    if d == 1 or d == 2: ### 위 아래 방향일 경우
        sharkmap[r-1][c-1].append((s%(2*R-2),d-1,z)) ### 내가 가지고 있는 배열과 dirlst에 맞게 변형해서 입력
    else:
        sharkmap[r-1][c-1].append((s%(2*C-2),d-1,z))

### 방향리스트 생성
dirlst = [(-1,0), (1,0), (0,1), (0,-1)] ### 위, 아래, 우, 좌

idx = 0 ### 낚시왕 위치

answer = 0

while idx<C:
    ### 상어 잡기
    for i in range(R): ### 땅에서부터 가까운거 찾기
        if sharkmap[i][idx]:
            answer += sharkmap[i][idx][0][-1]
            sharkmap[i][idx].clear()
            break ### 잡으면 바로 break


    ### 상어 이동
    newmap = [[[] for _ in range(C)] for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if sharkmap[i][j]:
                speed, sd, size = sharkmap[i][j][0]
                # print(i, j, sd)
                if sd in [0,1]:
                    newi, newj = i,j
                    for _ in range(speed):
                        # print('이동', newi, newj, sd)
                        if newi == 0 and sd == 0: sd=1
                        if newi == R-1 and sd == 1: sd=0
                        di, dj = dirlst[sd]
                        newi, newj = newi+di, newj+dj
                else:
                    newi, newj = i,j
                    for _ in range(speed):
                        if newj == 0 and sd == 3: sd=2
                        if newj == C-1 and sd == 2: sd = 3
                        di, dj = dirlst[sd]
                        newi, newj = newi+di, newj+dj
                # print(newi,newj)
                if newmap[newi][newj]:
                    if size > newmap[newi][newj][0][-1]:
                        newmap[newi][newj] = [(speed,sd,size)]
                else:
                    newmap[newi][newj].append((speed,sd,size))

    sharkmap = newmap

    idx += 1
print(answer)