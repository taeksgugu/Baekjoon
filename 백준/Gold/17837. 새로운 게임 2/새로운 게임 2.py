import sys
input = sys.stdin.readline
### 입력 받기
N, K = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]
horseposition = {i: list(map(lambda x: int(x)-1, input().rstrip().split())) for i in range(1,K+1)}
visited = {(horseposition[num][0], horseposition[num][1]): [num]  for num in range(1, K+1)}
# print(horseposition)
# print(visited)
### 방향리스트
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
            # print(i, hlst, ni,nj)
            if ni<0 or ni>=N or nj<0 or nj>=N or arr[ni][nj] == '2': ### 체스판 벗어날 경우, 파란색과 같이 대하기
                # print('파랑', )
                hdir = changedir[hdir]
                horseposition[i][2] = hdir
                ni, nj = hi+dirlst[hdir][0], hj+dirlst[hdir][1]
                if ni < 0 or ni >= N or nj < 0 or nj >= N or arr[ni][nj] == '2': ### 또 파란색이거나 벗어나면,,,,
                    continue
            ### 최종 방향이 결정된 경우-> 파란색이었어도 방향을 바꾸고 다시 진행
            if 0<=ni<N and 0<=nj<N: ### 무조건 움직임 (흰, 빨)
                visited[(hi, hj)] = visited[(hi, hj)][:visited[(hi, hj)].index(i)]  ### 원래 위치에 있던 말들 리스트 갱신
                if arr[ni][nj] == '0': ### 흰색이라면?
                    try: visited[(ni,nj)] += hlst
                    except: visited[(ni,nj)] = hlst
                    if len(visited[(ni,nj)]) >= 4:
                        return turn
                else: ### 빨간색
                    try: visited[(ni,nj)] += hlst[::-1]
                    except: visited[(ni,nj)] = hlst[::-1]
                    if len(visited[(ni,nj)]) >= 4:
                        return turn
                for horsenum in hlst: # 옮겨진 말들 위치 갱신
                    horseposition[horsenum] = [ni,nj,horseposition[horsenum][2]]
            # print(i, hlst)
            # print(horseposition)
            # print(visited)

        # print('해당 턴',turn)
        # print()
        turn += 1
    return -1
print(newgame())