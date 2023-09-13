### 1차 시도: 206240kb 1276ms 풀이 시간: 30분
### 초기 풀이 과정
### 우선 인구 차이를 확인하면서 딕셔너리형태로 그래프를 생성하고, 국경선이 열려야할 경우마다 cnt+1을 진행
### 만약 cnt가 0이라면 이동 불가 상태로 멈추게 지정
### 이후 연합이 여러개일 가능성을 두고 island 몇 개인지 확인하듯이 몇개인지 확인하고 인구 이동 진행
### 2차 시도: 205832kb 1244ms
### 시간 단축을 위해 연합별 리스트를 생성하지 않고 연합을 확인하자마자 인구 배정하는 방식으로 변경 -> 연합별 리스트를 순회할 필요가 없기 때문에 간편함
### 2번 제출했는데 한번은 더 걸림... 유의미한 차이가 없음
### 3차 시도: 120960kb 780ms
### graph를 생성하고 움직이는 것보다 처음부터 bfs를 하되 인구 차가 L이상 R이하인 경우를 넣어서 돌린다면 더욱더 줄일 수 있다고 판단
### 개선하는 과정에서 새로운 인구 배정을 할 때 실수로 = 이 아닌 ==을 입력해서 테케 해결에 시간이 걸림
### 4차 시도:
### unitednum 선언을 하지 않고 idx를 연장해서 사용

### 문제 후기 : 구현에 난이도는 없었지만 풀면 풀수록 더 최적화할 수 있다는걸 알게 됨. 풀이 과정을 한번 보고 더 최적화하는 방안 고려 필요
import sys
input = sys.stdin.readline
### 입력
N, L, R = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

def solve():
    day = 0
    while True:
        ### 두 나라 인구 차이
        checkv = [[0]*N for _ in range(N)] ### 체크여부 확인 배열
        cnt = 0 ### 국경선 열리는 수 확인
        for i in range(N):
            for j in range(N):
                if checkv[i][j] == 0:
                    united, total, idx = [(i,j)], arr[i][j], 0 ### 연합리스트 / 총 인구 수 / 순회할 인덱스번호
                    checkv[i][j] = 1 ### 다른 칸에 가도 해당 칸은 체크할 필요 없음
                    while idx<len(united):
                        ci, cj = united[idx]
                        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                            ni, nj = ci+di, cj+dj
                            if 0<=ni<N and 0<=nj<N and checkv[ni][nj] == 0:
                                if L<=abs(arr[ni][nj]-arr[ci][cj])<=R: ### 인구 차가 L이상 R이하라면
                                    united.append((ni,nj))
                                    checkv[ni][nj] = 1
                                    total += arr[ni][nj]
                        idx += 1 ### while문 벗어나면 idx가 곧 연합리스트 길이
                    newnum = total//idx ### 새로 배정할 인구수

                    if idx > 1: ### 국경선이 열릴 연합이 있다는 말
                        for ki, kj in united:
                            arr[ki][kj] = newnum
                        cnt += 1
        if not cnt: ### 국경선이 열릴게 없기 때문에 인구 이동이 발생하지 않고 바로 멈춤
            return day
        day += 1         ### 하루 지남
print(solve())