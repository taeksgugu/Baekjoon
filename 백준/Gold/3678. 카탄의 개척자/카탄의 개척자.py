import sys
input = sys.stdin.readline

### 어떤 타일 오는지 확인하는 함수
def checktile():
    for i in range(1, 6):
        avail[i] = False
    for i in range(6):
        di, dj = dirlst[i]
        nx, ny = sx+di, sy+dj
        val = arr[ny][nx]
        if val != 0:
            avail[val] = True
    maxi = 10000
    idx = 0
    for i in range(1, 6):
        if not avail[i]:
            if num[i] < maxi:
                maxi = num[i]
                idx = i
    arr[sy][sx] = idx
    num[idx] += 1
    number.append(idx)

def cal():
    global level, sx, sy
    while level < 61:
        sx += 1
        sy -= 1
        checktile()
        if cnt == 10001:
            break
        for i in range(level - 1):
            di, dj = dirlst[0]
            sx += di
            sy += dj
            checktile()
            if cnt == 10001:
                break
        for k in range(1, 6):
            for i in range(level):
                di, dj = dirlst[k]
                sx += di
                sy += dj
                checktile()
                if cnt == 10001:
                    break
        level += 1

T = int(input())
arr = [[0] * 301 for _ in range(601)]
number = [0]
level, sx, sy, cnt = 1, 150, 300, 1
dirlst = [(0,-2), (-1,-1), (-1,1), (0,2), (1,1), (1,-1)]
num = [0, 1, 0, 0, 0, 0]
avail = [False] * 6
arr[sy][sx] = 1
number.append(1)

cal()
for _ in range(T):
    target = int(input())
    print(number[target])
