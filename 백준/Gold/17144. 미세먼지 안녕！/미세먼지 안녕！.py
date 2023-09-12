import sys
input = sys.stdin.readline
### 입력 받기
R, C, T = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(R)]
aircleaner = [] ### 공기 청정기 좌표 입력
for i in range(R):
    for j in range(C):
        if arr[i][j] == -1:
            aircleaner.append(i)
up,down = aircleaner
### 시간 초기화
t = 1
while t<=T: ### T초 지날 때까지
    newarr = [[0]*C for _ in range(R)]
    ### 미세먼지 확장 구현
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0: ### 해당 칸에 미세먼지가 있다면
                total, remain = arr[i][j], arr[i][j]
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<R and 0<=nj<C and arr[ni][nj] != -1: ### 칸이 있고, 공기청정기가 없는 경우
                        newarr[ni][nj] += total//5
                        remain -= total//5
                newarr[i][j] += remain

    ### 청정기 작동 구현
    arr = [e[:] for e in newarr]
    up_arr = newarr[:down]
    down_arr = newarr[down:]
    for i in range(R):
        for j in range(C):
            if i == 0 or i == R-1:
                if j != C-1:
                    arr[i][j] = newarr[i][j+1]
                else:
                    if i == 0:
                        arr[i][j] = newarr[i+1][j]
                    else:
                        arr[i][j] = newarr[i-1][j]
            elif j == 0:
                if i <= up:
                    arr[i][j] = newarr[i-1][j]
                else:
                    arr[i][j] = newarr[i+1][j]
            elif j == C-1:
                if i <= up:
                    if i != up:
                        arr[i][j] = newarr[i+1][j]
                    else:
                        arr[i][j] = newarr[i][j-1]
                else:
                    if i != down:
                        arr[i][j] = newarr[i-1][j]
                    else:
                        arr[i][j] = newarr[i][j-1]
            elif i == up or i == down:
                arr[i][j] = newarr[i][j-1]
    arr[up][0], arr[down][0] = -1, -1

    t += 1

print(sum(map(sum,arr)) + 2)  ### 2를 더하는 이유는 공기청정기 부분이 -1이기 때문