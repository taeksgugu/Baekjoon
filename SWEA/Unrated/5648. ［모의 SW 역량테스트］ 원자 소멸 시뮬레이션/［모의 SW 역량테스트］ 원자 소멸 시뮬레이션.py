T = int(input())
for tc in range(1, T+1):
    N = int(input())
    dirlst = [(0,1), (0,-1), (-1,0), (1,0)]
    atomlst = []
    for _ in range(N):
        x, y, d, K = map(int, input().split())
        atomlst.append(((x+1000)*2, (y+1000)*2, d, K))
    # print(atomlst)
    totalscore = 0
    while True: ### 끝까지 진행 (0.5초 단위를 1초로 봄, 그대신 위에서 좌표 *2 진행)
    # for _ in range(3):
        ### 원자 이동
        resultlst = {}
        for ai, aj, ad, ak in atomlst:
            di, dj = dirlst[ad]
            ni, nj = ai+di, aj+dj
            if 0<=ni<4001 and 0<=nj<4001:
                if resultlst.get((ni,nj)): resultlst[(ni,nj)].append((ad, ak))
                else: resultlst[(ni,nj)] = [(ad,ak)]

        ### 충돌 여부 확인 및 다음 턴 넘길
        newatomlst = []
        for ci, cj in resultlst:
            lst = resultlst[(ci,cj)]
            if len(lst) == 1: ### 하나라면
                cd, ck = lst[0]
                newatomlst.append((ci, cj, cd, ck))
            else:
                deletepower = 0
                for _, ck in lst:
                    deletepower += ck
                totalscore += deletepower
        # print(resultlst)
        if len(newatomlst) == 0: break
        atomlst = newatomlst

    print(f"#{tc} {totalscore}")