### 1차 시도 : 시간 초과 풀이시간 20분
### 2차 시도 : 시간 초과
### 3차 시도 :
import sys
input = sys.stdin.readline
### 입력 받기
N = int(input().rstrip())
arr = [input().rstrip().split() for _ in range(N)]
dp_dir = [[[0]*3 for _ in range(N)] for _ in range(N)]
### 1열은 무조건 다 0, 1행은 무조건 1
### 가로: 0, 세로: 1, 대각선: 2
for j in range(1,N):
    if arr[0][j] == '0':
        dp_dir[0][j][0] = 1
    else: break

### 해당 칸은 무조건 왼쪽 대각선 칸에 가는 방법 수와 윗칸의 가는 방법 수의 합으로 구성됨
for i in range(1,N):
    for j in range(1, N):
        if arr[i][j] == '0': ### 벽이 아니라면
            if arr[i-1][j] == '0' and arr[i][j-1] == '0':
                dp_dir[i][j][2] += sum(dp_dir[i-1][j-1]) ### 대각선은 다 받기
            dp_dir[i][j][1] += (dp_dir[i-1][j][1]+dp_dir[i-1][j][2])
            dp_dir[i][j][0] += (dp_dir[i][j-1][0]+dp_dir[i][j-1][2])

# for l in dp_dir:
#     print(l)
print(sum(dp_dir[-1][-1]))