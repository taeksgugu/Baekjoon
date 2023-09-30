
### 기본 관리 변수 설정 & 함수 생성
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]
changedir = {1:[1,3,0,2], 2: [3,0,1,2], 3:[2,0,3,1], 4:[1,2,3,0], 5:[1,0,3,2]}
def pinball(si,sj,sd):
    stoplst = blackhole + [(si,sj)]
    score = 0
    while True:
        di, dj = dirlst[sd]
        si, sj =si+di, sj+dj
        if (si, sj) in stoplst:  ### 출발지로 돌아오거나 블랙홀에 빠지면
            return score
        if 1<=arr[si][sj]<=5: ### 블록이면
            sd = changedir[arr[si][sj]][sd]
            score += 1
        elif 6<=arr[si][sj]<=10: ### 웜홀이면
            lst = wormhole[arr[si][sj]]
            if (si,sj) == lst[0]: si, sj = lst[1]
            else: si, sj = lst[0]

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [[5]*(N+2)] + [[5] + list(map(int, input().split())) +[5] for _ in range(N)] + [[5]*(N+2)]
    blackhole = [] ### 블랙홀 리스트
    wormhole = {} ### 웜홀 딕셔너리
    emptylst = [] ### 빈칸들 (핀볼 출발 리스트)
    for i in range(1, N+1):
        for j in range(1, N+1):
            if arr[i][j] == 0: emptylst.append((i,j))
            elif arr[i][j] == -1: blackhole.append((i,j))
            elif arr[i][j] >= 6: ### 웜홀이라면
                if wormhole.get(arr[i][j]): wormhole[arr[i][j]].append((i,j))
                else: wormhole[arr[i][j]] = [(i,j)]

    totalscore = 0
    for si, sj in emptylst: ### 빈칸 중 핀볼 출발 위치 선정
        for sd in range(4):
            # print('시작', si,sj,sd)
            nowscore = pinball(si,sj,sd)
            totalscore = max(totalscore, nowscore)

    print(f"#{tc} {totalscore}")