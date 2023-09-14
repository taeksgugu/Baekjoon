import sys
input = sys.stdin.readline
C, R = map(int, input().rstrip().split())
K = int(input().rstrip())

def seat():
    move = 0
    i, j = 1, 0
    dir = 0  ### 상:0 우:1 하:2 좌:3
    x, y = R, C - 1  ### 방향 컨트롤 수
    if K > R*C:
        return 0
    while x>0 or y>0:
        if dir == 0 or dir == 2: ## 상하로 움직일 때
            for _ in range(x,0,-1):
                if dir == 0:
                    j += 1
                else:
                    j -= 1
                move += 1
                if move == K:
                    return i,j
            x -= 1
            dir += 1 ### 다음 방향으로
        if dir == 1 or dir == 3:
            for _ in range(y,0,-1):
                if dir == 1:
                    i += 1
                else:
                    i -= 1
                move += 1
                if move == K:
                    return i,j
            y -= 1
            dir = (dir+1)%4

    return i,j

answer = seat()
if answer == 0:
    print(answer)
else:
    print(answer[0], answer[1])