### 초기 풀이과정 : 먼저 사다리 게임을 그려봐서 체제를 이해하고 제일 먼저 출발해서 도착하는 걸 구현해야겠다고 생각함
### 1차 시도: 시간초과 풀이 시간 50분
### 2차 시도: 시간초과 풀이 시간 10분
###          시간 단축을 위해 왼쪽 사다리 제거 & if문 실수 확인해서 바꿈
### 3차 시도: 시간초과 풀이 시간 5분
###          사다리 내려가기 함수를 재귀 돌기 전에 입력함으로써 시간 단축 시도 (% 올라가는건 빨라졌지만,,, 마의 8%를 못 넘김)
### 4차 시도: 시간초과 풀이 시간 5분
###          사다리 조합을 만드는 거에서 가지치기를 더 해야한다고 판단
###          jdx라는 변수를 추가해서 재귀를 덜 돌게 만듦 (기존에 하려다가 실수 가능성 때문에 안함)
### 5차 시도: 시간초과 풀이 시간 15분
###          처음부터 인접 사다리 부분도 방문처리함으로써 백트래킹 계산량 줄임
### 6차 시도: 시간초과 풀이 시간 17분
###          내 가정이 맞는지 모르겠지만 추가되는 사다리가 바꿀 수 있는 결과의 갯수는 사다리 행 번호*2개임
### 7차 시도: 시간초과 풀이 시간 3분
###          사다리 내리는 과정이  cnt를 추가하면서 길어진거 같아서 방문처리를 통해 줄였으나 마의 8%를 못 넘김
### 8차 시도: 시간초과 풀이 시간 5분
###          혹시 처음부터 아예 안될 가능성을 생각하고 case를 추가했지만 역시 시간초과
### 9차 시도:
###          모든 코드를 지우고 처음부터 다시 작성함 (방식은 아무리 생각해도 맞는 것 같아서 최적화에 집중)
###          방문처리를 하는게 아니라 방문처리와 사다리 이동을 같이 하는 배열을 만들어서 최적화를 진행해보자
###          출발점과 도착점이 같은 경우를 count 하는 함수를 사용하면 속도가 더 느려지는 것 같음. 그냥 원래 기존 방식을 유지
###          평소와는 다르게 flag 사용함 평소에는 go=True였는데 이번엔 flag=False로 사용
###          이렇게 푸니깐 오히려 더 간결해지고 이뻐짐 코드가
### 입력 받기
N, M, H = map(int, input().split())
visited = [[0] * (H + 1) for _ in range(N + 1)]
for _ in range(M): ### 사다리 방문처리
    a, b = map(int, input().split())
    visited[b][a] = b+1 ### 오른쪽
    visited[b+1][a] = b ### 왼쪽

### 출발점 도착점 확인 함수
def ladder():
    for num in range(1, N+1):
        idx = num
        for j in range(1, H+1):
            if visited[idx][j]: idx = visited[idx][j]
        if idx != num:
            return False
    return True

### 본격 완탐 시작...
answer = N*H ### answer은 최댓값
def solve(cnt):
    global answer
    if ladder(): ### 된다면 갱신
        answer = min(answer, cnt)
    elif cnt == 3 or answer <= cnt: ### 최소한의 가지치기
        return
    for i in range(1, N):
        flag = False
        for j in range(1, H+1):
            if flag and visited[i][j] == 0 and visited[i+1][j] == 0: continue  
            else: flag = False
            if visited[i][j] == 0 and visited[i+1][j] == 0:
                visited[i][j] = i + 1
                visited[i+1][j] = i
                solve(cnt+1)
                visited[i][j] = 0
                visited[i+1][j] = 0
                flag = True
solve(0)
if answer <= 3: print(answer)
else: print(-1)