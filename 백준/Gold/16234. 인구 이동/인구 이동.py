### 1차 시도: 206240kb 1276ms 풀이 시간: 30분
### 초기 풀이 과정
### 우선 인구 차이를 확인하면서 딕셔너리형태로 그래프를 생성하고, 국경선이 열려야할 경우마다 cnt+1을 진행
### 만약 cnt가 0이라면 이동 불가 상태로 멈추게 지정
### 이후 연합이 여러개일 가능성을 두고 island 몇 개인지 확인하듯이 몇개인지 확인하고 인구 이동 진행
### 2차 시도: 205832kb 1280ms 
### 시간 단축을 위해 연합별 리스트를 생성하지 않고 연합을 확인하자마자 인구 배정하는 방식으로 변경 -> 연합별 리스트를 순회할 필요가 없기 때문에 간편함
### 오히려 오래 걸림.... 이유는 모르겠음...

import sys
from collections import deque
input = sys.stdin.readline
### 입력
N, L, R = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

def solve():
    day = 0
    while True:
        ### 두 나라 인구 차이 확인
        graph = {(a, b): [] for a in range(N) for b in range(N)} ### 국경선 열어야할 그래프 생성
        checkv = [[0]*N for _ in range(N)] ### 체크여부 확인 배열
        cnt = 0 ### 국경선 열리는 수 확인
        for i in range(N):
            for j in range(N):
                checkv[i][j] = 1 ### 다른 칸에 가도 해당 칸은 체크할 필요 없음
                peoplenum = arr[i][j]
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and checkv[ni][nj] == 0:
                        if L<=abs(arr[ni][nj]-peoplenum)<=R: ### 인구 차가 L이상 R이하라면
                            graph[(i,j)].append((ni,nj))
                            graph[(ni,nj)].append((i,j))
                            cnt += 1
        if not cnt: ### 국경선이 열릴게 없기 때문에 인구 이동이 발생하지 않고 바로 멈춤
            return day

        ### 연합 수 확인
        visited = [[0]*N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                if graph[(i,j)] and visited[i][j] == 0: ### 국경선이 열린 국가라면 연합의 스타트 & 이미 연합 처리 안한 국가
                    q = deque()
                    q.append((i,j))
                    total = arr[i][j] ### 인구 합 구하는 변수
                    nearlst = [(i,j)] ### 같이 연합인 국가 리스트
                    visited[i][j] = 1
                    while q:
                        ci, cj = q.popleft()
                        for neari, nearj in graph[(ci,cj)]:
                            if visited[neari][nearj] == 0:
                                visited[neari][nearj] = 1 ### 방문처리
                                q.append((neari, nearj))    ### q에 추가
                                nearlst.append((neari, nearj))     ### 같은 연합 처리
                                total += arr[neari][nearj]        ### 인구 합 처리
                    newnum = total//len(nearlst)
                    for ki, kj in nearlst:
                        arr[ki][kj] = newnum

        ### 하루 지남
        day += 1

print(solve())