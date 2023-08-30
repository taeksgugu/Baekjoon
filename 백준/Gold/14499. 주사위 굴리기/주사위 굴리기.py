import sys
input = sys.stdin.readline
### 값 입력받기
N, M, X, Y, K = map(int, input().rstrip().split())
arr = [input().split() for _ in range(N)]
orderlst = list(map(int, input().rstrip().split()))
### 주사위 전개도 만들기
dice = ['0']*6 ### 여기서 항상 윗면은 dice[0]임, 아랫면은 dice[-1]
dirlst = [(0,1), (0,-1), (-1,0), (1,0)]
dicelst = [[2,1,5,0,4,3],[3,1,0,5,4,2],[1,5,2,3,0,4],[4,0,2,3,5,1]]
def game():
    global dice
    ci, cj = X, Y
    for order in orderlst: ### 순서대로 명령 수행
        di, dj = dirlst[order-1]
        ni, nj = ci+di, cj+dj
        if 0<=ni<N and 0<=nj<M: ### 지도 안이라면 이동
            dice = [dice[i] for i in dicelst[order-1]]
            mapnum = arr[ni][nj]  ### 지도 해당 칸 번호
            if mapnum != '0': ### 지도 칸이 0이 아니라면
                dice[-1] = mapnum ### 주사위칸 변경
                arr[ni][nj] = '0' ### 0으로 초기화
                ci, cj = ni, nj ### 주사위 위치 변경
            else: ### 0이면 다이스 ㅋ칸 번호로 바꾸기
                arr[ni][nj] = dice[-1]
                ci, cj = ni, nj
            print(dice[0])
game()