import sys
input = sys.stdin.readline
M, N = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]
def robot(arr):
    x, y, direction = 0, 0, 'right'
    for idx in range(N):
        action, val = arr[idx]
        ## 움직이라는 명령일 때
        if action == 'MOVE':
            if direction == 'right': ## 방향이 오른쪽
                y += int(val)
            elif direction == 'left': ## 방향이 왼쪽
                y -= int(val)
            elif direction == 'top': ## 방향이 위쪽
                x += int(val)
            else: ### 방향이 아래쪽
                x -= int(val)
        else: ### 회전하라는 명령일 때
            if int(val) == 0: ## 왼쪽 회전
                if direction == 'right':
                    direction = 'top'
                elif direction == 'left':
                    direction = 'bottom'
                elif direction == 'top':
                    direction = 'left'
                else:
                    direction = 'right'
            else: ## 오른쪽 회전
                if direction == 'right':
                    direction = 'bottom'
                elif direction == 'left':
                    direction = 'top'
                elif direction == 'top':
                    direction = 'right'
                else:
                    direction = 'left'
        if 0<=x<=M and 0<=y<=M:
            continue
        else:
            return [-1]
    return [y, x]
print(*robot(arr))