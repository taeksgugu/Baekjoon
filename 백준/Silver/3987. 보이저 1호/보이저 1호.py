import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
## 전체 항성계 지도 받아오기
arr = [['C']*(M+2)] + [['C'] + list(input().rstrip()) + ['C'] for _ in range(N)] + [['C']*(M+2)]
## 시작 위치 받아오기
start_x, start_y = map(int, input().rstrip().split())
## 전파 보냈을 때 최대 시간 구하는 함수 생성
def rocket(x,y,direction):
    cnt = 0
    while True:
        cnt += 1
        ### 무한히 순환할 때 탈출 조건
        if cnt > N*M*2:
            return 'Voyager'
        ### 한칸 이동
        if direction == 'U':
            x -= 1
        elif direction == 'R':
            y += 1
        elif direction == 'D':
            x += 1
        else:
            y -= 1
        ### 블랙홀 만나버림
        if arr[x][y] == 'C':
            return cnt
        else:
            ### 방향 change
            if arr[x][y] == '/':
                if direction == 'U':
                    direction = 'R'
                elif direction == 'R':
                    direction = 'U'
                elif direction == 'D':
                    direction = 'L'
                else:
                    direction = 'D'
            elif arr[x][y] == '\\':
                if direction == 'U':
                    direction = 'L'
                elif direction == 'R':
                    direction = 'D'
                elif direction == 'D':
                    direction = 'R'
                else:
                    direction = 'U'

ans = 0
for dir in ['U', 'R', 'D', 'L']:
    res = rocket(start_x, start_y, dir)
    if res == 'Voyager':
        ans_dir = dir
        ans = res
        break
    elif res > ans:
        ans_dir = dir
        ans = res
print(ans_dir)
print(ans)