import sys, math
input = sys.stdin.readline

N, K = map(int, input().split())
lst = list(map(int, input().rstrip().split()))

roundnum = 1


def snail():
    arr = [[lst[0]], lst[1:]]
    # for l in arr:
    #     print(l)
    while True:
        # print(arr)
        fullength = len(arr)
        length = len(arr[-2])
        if len(arr[-1]) - length < fullength: break
        head = [x[:length] for x in arr]
        head = [x[::-1] for x in list(map(list, zip(*head)))]
        tail = [arr[-1][length:]]
        # print('머리', head)
        # print('꼬리', tail)
        # print()
        arr = head + tail

    return arr
while True:
    # print(roundnum)
    ### 물고기의 수가 가장 적은 어항에 물고기를 한 마리 넣는다
    minfish = min(lst)
    for i in range(N):
        if lst[i] == minfish: lst[i] += 1
    ### 디버깅
    # print('최소추가')
    # print(lst)
    # ### 공중 부양

    arr = snail()

    # ### 디버깅
    # print('달팽이화')
    # for l in arr:
    #     print(*l)
    ### 물고기 조절
    controlarr = [[0]*len(arr[row]) for row in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            num = arr[i][j]
            for di, dj in [(0,1), (1,0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<len(arr) and 0<=nj<len(arr[i]):
                    othernum = arr[ni][nj]
                    dnum = abs(num - othernum) // 5
                    if dnum > 0:
                        if num > othernum:
                            controlarr[i][j] -= dnum
                            controlarr[ni][nj] += dnum
                        else:
                            controlarr[i][j] += dnum
                            controlarr[ni][nj] -= dnum
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            arr[i][j] += controlarr[i][j]

    ### 디버깅
    # print('물고기 조절 후')
    # for l in arr:
    #     print(*l)
    # print()
    ### 펼치기
    newlst = []
    for j in range(len(arr[-1])):
        for i in range(len(arr)-1, -1, -1):
            if j < len(arr[i]):
                newlst.append(arr[i][j])


    ### 디버깅
    # print('평평')
    # print(newlst)


    ### 2차 공중 부양
    newlength = len(newlst)
    arr = [newlst[:newlength//2][::-1], newlst[newlength//2:]]

    firstarr = [x[:newlength//4] for x in arr]
    firstarr = [x[::-1] for x in firstarr[::-1]]
    secondarr = [x[newlength//4:] for x in arr]
    arr = firstarr + secondarr
    ### 디버깅
    # print('2차 공중')
    # for l in arr:
    #     print(*l)

    ### 물고기 작업 한 번 더
    controlarr = [[0]*len(arr[0]) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            num = arr[i][j]
            for di, dj in [(0,1), (1,0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<len(arr) and 0<=nj<len(arr[0]) and arr[ni][nj] != -1:
                    othernum = arr[ni][nj]
                    dnum = abs(num - othernum) // 5
                    if dnum > 0:
                        if num > othernum:
                            controlarr[i][j] -= dnum
                            controlarr[ni][nj] += dnum
                        else:
                            controlarr[i][j] += dnum
                            controlarr[ni][nj] -= dnum
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            arr[i][j] += controlarr[i][j]

    ### 디버깅
    # print('2차 조절')
    # for l in arr:
    #     print(*l)

    # lst = []
    # for j in range(len(arr[0])):
    #     for i in range(len(arr)-1,-1,-1):
    #         lst.append(arr[i][j])
    arr = [x[::-1] for x in list(map(list, zip(*arr)))]
    lst = [x for y in arr for x in y]

    ### 디버깅
    # print(lst)

    ### 최종 확인
    if max(lst)-min(lst) <= K:
        print(roundnum)
        break

    else:
        roundnum += 1
