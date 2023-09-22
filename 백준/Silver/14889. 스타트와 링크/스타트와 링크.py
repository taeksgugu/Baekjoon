### 9월 22일 재풀이
### 1차 시도 : 시간 초과 / 9시 30분 start 9시 40분 finish
###           진짜 생각없이 범위 고려하지 않음...
### 2차 시도, 3차 시도 : 시간 초과
### 초기 풀이과정 : 재귀를 이용해 처음부터 두팀을 나누면서 들어갈 예정
###               그리고 N/2로 팀이 나눠지면 차이를 구해서 최솟값 갱신 방식으로 진행 예정

### 예전에 풀이했던 방식은 한 팀만 고려해서 진행함
### 이번 풀이 방식은 두 팀을 같이 했는데 시간초과가 계속 발생해서 테스트해봄
### 1,2 & 3,4 와 3,4&1,2 가 같은 경우이기 때문에 이전 방식보다 2배 시간 더 소모
### 해결 방법은 for문을 사용하지 않는 것! 할 필요가 없는 것 무조건 넣는거니깐

import sys
input = sys.stdin.readline
### 입력 받기
N = int(input())
arr = [list(map(int, input().strip().split())) for _ in range(N)]

answer = 4000 ### 최대 20명, 능력치 차 최대 99 그래서 걍 20*100*2로 정함
def maketeam(n, A, B): ### 총 뽑은 인원수, 스타트 팀, 링크 팀
    global answer
    if answer == 0: return ### 이미 최솟값
    if abs(len(A)-len(B)) > N-n: ### 남은 인원을 다 투입해도 팀 밸런스 안 맞는 경우
        return
    if n == N: ### 종료조건(다 뽑으면)
        if len(A) == len(B): ### 같은 인원 선발
            Ascore, Bscore = 0, 0 ### 두팀 능력치 변수
            for i in range(N//2-1):
                for j in range(i, N//2):
                    Ascore += (arr[A[i]][A[j]]+arr[A[j]][A[i]])
                    Bscore += (arr[B[i]][B[j]]+arr[B[j]][B[i]])
            answer = min(answer, abs(Ascore-Bscore))
        return

    maketeam(n+1, A+[n], B)
    maketeam(n+1, A, B+[n])

maketeam(0,[],[])
print(answer)
