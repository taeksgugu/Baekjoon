import sys
# from collections import deque
input = sys.stdin.readline
### 톱니바퀴 회전 수행 목록 만들기
def makelst(num, direction):
    changelst = [(num-1, direction)]
    if num == 1: ## 1번 톱니바퀴
        if arr[0][2] != arr[1][-2]:
            changelst.append((1,direction*(-1)))
            if arr[1][2] != arr[2][-2]:
                changelst.append((2, direction))
                if arr[2][2] != arr[3][-2]:
                    changelst.append((3, direction * (-1)))
    elif num == 2: ## 2번 톱니바퀴
        if arr[1][-2] != arr[0][2]:
            changelst.append((0,direction*(-1)))
        if arr[1][2] != arr[2][-2]:
            changelst.append((2, direction * (-1)))
            if arr[2][2] != arr[3][-2]:
                changelst.append((3, direction))
    elif num == 3: ### 3번 톱니바퀴
        if arr[2][2] != arr[3][-2]: # 4번
            changelst.append((3,direction*(-1)))
        if arr[2][-2] != arr[1][2]: # 2번
            changelst.append((1, direction * (-1)))
            if arr[1][-2] != arr[0][2]: # 1번
                changelst.append((0, direction))
    else:
        if arr[3][-2] != arr[2][2]:
            changelst.append((2,direction*(-1)))
            if arr[2][-2] != arr[1][2]:
                changelst.append((1, direction))
                if arr[1][-2] != arr[0][2]:
                    changelst.append((0, direction * (-1)))
    return changelst
### 톱니바퀴 회전하기
def roll(changelst):
    for num, direction in changelst:
        lst = arr[num]
        if direction == -1:
            lst.append(lst.pop(0))
        else:
            lst = [lst.pop()] + lst
        arr[num] = lst
### 톱니바퀴 입력받기
arr = [list(input().rstrip()) for _ in range(4)]
K = int(input().rstrip())
for _ in range(K):
    num, direction = map(int, input().rstrip().split())
    l = makelst(num, direction)
    roll(l)
    # print(num ,direction, l)
    # for qqq in arr:
    #     print(''.join(qqq), qqq[-2],qqq[2])
    # print(*arr)
answer = 0
for i in range(4):
    if arr[i][0] == '1': ### S극이면
        answer += (2**i)
print(answer)