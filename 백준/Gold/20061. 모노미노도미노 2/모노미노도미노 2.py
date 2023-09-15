import sys
input = sys.stdin.readline

N = int(input())
blocklst = [list(map(int, input().rstrip().split())) for _ in range(N)]

blue = [[0]*6 for _ in range(4)]
green = [[0]*4 for _ in range(6)]
totalscore = 0

# t, x, y = 1, 1, 1
# t, x, y = 2, 3, 0
# t, x, y = 3, 2, 2
# blocklst = [[t,x,y]]
for t, x, y in blocklst:
    ### 블럭 쌓기 우선
    if t == 1:### t == 1
        ### 파란색 보드 처리
        bi, bj = x, -1
        for _ in range(7):
            if 0<=bj+1<6 and blue[bi][bj+1] == 0:
                bj += 1
            else:
                blue[bi][bj] = 1
                break
        ### 초록색 보드 처리
        gi, gj = -1, y
        for _ in range(7):
            if 0<=gi+1<6 and green[gi+1][gj] == 0:
                gi += 1
            else:
                green[gi][gj] = 1
                break
    elif t==2: ### t == 2
        bi, bj = x,0
        for _ in range(6):
            if 0<=bj+1<6 and blue[bi][bj+1] == 0:
                bj += 1
            else:
                if bj != 0:
                    blue[bi][bj-1] = 1
                    blue[bi][bj] = 1
                    break
        gi, gj1, gj2 = -1, y, y+1
        for _ in range(7):
            if 0<=gi+1<6 and green[gi+1][gj1] == 0 and green[gi+1][gj2] == 0:
                gi += 1
            else:
                green[gi][gj1] = 1
                green[gi][gj2] = 1
                break
    else:
        ### 파란색 보드 처리
        bi1, bi2, bj = x, x+1, -1
        for _ in range(7):
            if 0<=bj+1<6 and blue[bi1][bj+1] == 0 and blue[bi2][bj+1] == 0:
                bj += 1
            else:
                blue[bi1][bj] = 1
                blue[bi2][bj] = 1
                break
        ### 초록색 보드 처리
        gi, gj = 0, y
        for _ in range(6):
            if 0<=gi+1<6 and green[gi+1][gj] == 0:
                gi += 1
            else:
                if gi != 0:
                    green[gi-1][gj] = 1
                    green[gi][gj] = 1
                    break

    # print('행열정리')
    ### 블루랑 그린 행 열 정리
    ### 블루부터
    blue_T = list(map(list, zip(*blue)))
    newblue = []
    for line in blue_T:
        if sum(line) == 4:
            newblue = [[0]*4] + newblue
            totalscore += 1
        else:
            newblue.append(line)
    ### 싹다돌고 연한 부분에 블럭 있는지 확인
    skybluecnt = 0 ### 지워야하는 행의 수
    if sum(newblue[0]) != 0: skybluecnt += 1
    if sum(newblue[1]) != 0: skybluecnt += 1
    for _ in range(skybluecnt):
        newblue.pop()
        newblue = [[0] * 4] + newblue
    blue = list(map(list, zip(*newblue)))
    ### 그린도
    newgreen = []
    for line in green:
        if sum(line) == 4:
            newgreen = [[0]*4] + newgreen
            totalscore += 1
        else:
            newgreen.append(line)
    skygreencnt = 0 ### 지워야하는 행의 수
    if sum(newgreen[0]) != 0: skygreencnt += 1
    if sum(newgreen[1]) != 0: skygreencnt += 1
    for _ in range(skygreencnt):
        newgreen.pop()
        newgreen = [[0] * 4] + newgreen
    green = newgreen
# for ll in blue:
#     print(*ll)
# print()
# for gg in green:
#     print(*gg)
print(totalscore)
print(sum([x for y in blue for x in y])+sum([x for y in green for x in y]))