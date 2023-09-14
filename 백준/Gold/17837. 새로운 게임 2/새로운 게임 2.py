### 초기 풀이 과정: -> 말번호별 위치와 해당 위치에 말들이 어떻게쌓여있는지를 관리해야한다고 생각했음
###             2개 다 딕셔너리로 관리하는게 편하다고 판단해서 딕셔너리 자료구조를 사용했고 처음에 입력 받을 때 초기 상태를 업데이트함
###             이동할 칸의 색별로 구현하려고 했으나, 파란색도 결국은 방향을 바꿔준다는 의미라고 판단해서 이동하는 부분은 합쳐서 구현함
### 실수한 부분 : 체스판 밖으로 나가는 부분 구현 과정에서 nj<0을 nj<N으로 적어서 에러가 발생함 (이 와중에 테케 많이 맞음..)
###             말이 이동할 때, 해당 말 위의 말들의 포지션 갱신 과정에서 실수로 옮겨지는 말의 방향으로 통일시켜버림 (마지막 테케 틀림)
### 1차 시도 : 118216kb 212ms 풀이: 1시간 10분
### 2차 시도 :
###           흰색 빨간색 구분 과정에서 굳이 두 파트로 나누지 않고 빨간색일 때만 옮기는 리스트를 뒤집어서 진행함 -> 코드 간결해짐
### 아쉬운 점 : 구현하는데 있어서 큰 어려움이 없었으나, 범위를 잘못 입력하는 우를 범하고 값 갱신 과정에서 변수를 잘못 입력함
### 괜찮은 점 : 이전 한수님 코드에서 배운 점을 오늘 잘 적용함 (try, except) -> 확인할 필요 없어서 편한 듯
###           항상 대부분 순서대로 구현하는 방식을 선호해서 디버깅이 편하고 중간중간 print를 넣어서 어느 부분이 잘못되는거 캐치하는게 편함
import sys
input = sys.stdin.readline
### 입력 받기
N, K = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]
horseposition = {i: list(map(lambda x: int(x)-1, input().rstrip().split())) for i in range(1,K+1)}
visited = {(horseposition[num][0], horseposition[num][1]): [num]  for num in range(1, K+1)}

### 게임 진행 함수
def newgame():
    dirlst= [(0,1), (0,-1), (-1,0), (1,0)] ### 우:0 좌:1 상:2 하:3
    changedir = {0:1, 1:0, 2:3, 3:2}
    turn = 1
    while turn <=1000:
        for i in range(1,K+1): ### 순서대로 이동
            hi, hj, hdir = horseposition[i] ### 해당 번호 말 위치&방향
            hlst = visited[(hi,hj)][visited[(hi,hj)].index(i):] ### 옮겨야할 말은 해당 위치에 있던 그 말 위에 있는 말들
            di, dj = dirlst[hdir]
            ni, nj = hi+di, hj+dj
            if ni<0 or ni>=N or nj<0 or nj>=N or arr[ni][nj] == '2': ### 체스판 벗어날 경우, 파란색과 같이 대하기
                hdir = changedir[hdir]
                horseposition[i][2] = hdir
                ni, nj = hi+dirlst[hdir][0], hj+dirlst[hdir][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == '2': ### 또 파란색이거나 벗어나면,,,,
                    continue
            ### 최종 방향이 결정된 경우-> 파란색이었어도 방향을 바꾸고 다시 진행
            if 0<=ni<N and 0<=nj<N: ### 무조건 움직임 (흰, 빨)
                visited[(hi, hj)] = visited[(hi, hj)][:visited[(hi, hj)].index(i)]  ### 원래 위치에 있던 말들 리스트 갱신
                if arr[ni][nj] == '1': ### 빨간색일 때 뒤집기, 흰색이면 그대로
                    hlst = hlst[::-1]
                try: visited[(ni,nj)] += hlst
                except: visited[(ni,nj)] = hlst
                if len(visited[(ni,nj)]) >= 4: ### 해당칸의 쌓인 말이 4개 이상이면 바로 break해버리기
                    return turn

                for horsenum in hlst: # 옮겨진 말들 위치 갱신
                    horseposition[horsenum] = [ni,nj,horseposition[horsenum][2]]
        turn += 1
    return -1
print(newgame())