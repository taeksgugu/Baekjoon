import sys
input = sys.stdin.readline
### 입력
dice = list(map(int, input().rstrip().split()))

###윳놀이 바깥줄 리스트 만들기
line = [i for i in range(0,42)] ### 0은 시작점, 41은 도착점
line10 = [10, '13', '16', '19', '25', '30', '35', 40, '41']
line20 = [20, '22', '24', '25', '30', '35', 40, '41']
line30 = [30, '28', '27', '26', '25', '30', '35', 40, '41']
line25 = ['25', '30', '35', 40, '41', '41', '41', '41', '41']

### 주사위 놀이 시작
answer = 0
def yoot(n, lst, score, belst):
    global answer
    # print(n, lst, score, edgecase)
    if n == 10: ### 종료조건
        # if answer < score:
        #     print(n, lst, score, belst)
        answer = max(answer, score)
        return

    ### 돌 선택해서 움직이기
    num = dice[n]
    for i in range(4):
        horse = lst[i]
        if int(horse) >= 41: continue ### 이미 도착한 말
        ### 해당 말이 파란색화살표를 사용했을 경우
        if horse in line25:
            idx = line25.index(horse)
            next = line25[idx + num]
        elif horse == 10 or horse in line10:
            idx = line10.index(horse)
            next = line10[idx + num]
        elif horse == 30 or horse in line30:
            idx = line30.index(horse)
            next = line30[idx + num]
        elif horse == 20 or horse in line20:
            idx = line20.index(horse)
            next = line20[idx + num]
        else:
            next = horse + num*2
        # print('다음', next, i)
        ### 이동할 칸에 다른 말 있는 경우 확인
        if int(next) < 41 and next not in lst: ### 다른 말이 해당 칸에 없으면 이동
            yoot(n+1, lst[:i]+[next]+lst[i+1:], score+int(next), lst)
        elif int(next) >= 41: ### 도착했을 경우
            # print('도착')
            yoot(n+1, lst[:i] + [41] + lst[i + 1:], score, lst)

yoot(0, [0,0,0,0],0,[])
# yoot(4, [28,28,28,28],0,[0,0,0,0])
print(answer)