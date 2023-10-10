def checkbattery(i,j):
    possible = []
    for bnum in range(1, A+1):
        bx, by, bc, bp = batterydict[bnum]
        dist = abs(bx-i) + abs(by-j)
        if dist<=bc: possible.append((bnum, batterydict[bnum][3]))
    return possible

def calmax(abattery, bbattery):
    abattery.sort(key=lambda x: -x[1])
    bbattery.sort(key=lambda x: -x[1])
    if abattery[0] != bbattery[0]: return abattery[0][1]+bbattery[0][1]
    else:
        if len(abattery) == 1 and len(bbattery) == 1:
            return abattery[0][1]
        elif len(abattery)==1:
            return abattery[0][1] + bbattery[1][1]
        elif len(bbattery)==1:
            return bbattery[0][1] + abattery[1][1]
        else:
            return bbattery[0][1] + max(abattery[1][1], bbattery[1][1])

# print(calmax([100, 360,240],[100, 360, 240]))
T = int(input())
for tc in range(1, T+1):
    M, A = map(int, input().split())
    lsta = [0] + list(map(int, input().split()))
    lstb = [0] + list(map(int, input().split()))
    batterydict = {}
    for num in range(1, A+1):
        x, y, c, p = map(int, input().split())
        batterydict[num] = (x,y,c,p)
    ai, aj, bi, bj = 1, 1, 10, 10
    dirlst = [(0,0), (0,-1), (1,0), (0,1), (-1,0)] # 제자리, 상, 우, 하, 좌
    totalpower = 0
    for idx in range(M+1):
        adi, adj = dirlst[lsta[idx]]
        bdi, bdj = dirlst[lstb[idx]]
        ai, aj = ai+adi, aj+adj
        bi, bj = bi+bdi, bj+bdj
        abattery = checkbattery(ai,aj)
        bbattery = checkbattery(bi,bj)
        if not abattery and not bbattery:
            # print(idx, 0)
            continue
        if not abattery:
            # print(idx, sorted(bbattery, reverse=True)[0])
            totalpower += sorted(bbattery, key=lambda x: -x[1])[0][1]
        elif not bbattery:
            # print(idx, sorted(abattery, reverse=True)[0])
            totalpower += sorted(abattery, key=lambda x: -x[1])[0][1]
        else:
            # print(idx, calmax(abattery, bbattery))
            totalpower += calmax(abattery,bbattery)
    print(f"#{tc} {totalpower}")