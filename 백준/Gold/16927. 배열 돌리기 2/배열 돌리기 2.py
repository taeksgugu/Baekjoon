import sys
input = sys.stdin.readline
N, M, T = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]

### 우:0 하:1 좌:2 상:3
def chk():
    move = 0
    R, C = N, M
    i, j = 0, -1
    dir = 0
    linelst = []
    while R>0 or C>0:
        if dir == 0:
            lst = []
        if dir == 0 or dir == 2:
            for _ in range(C,0,-1):
                if dir == 0:
                    j += 1
                else:
                    j -= 1
                lst.append(arr[i][j])
                move += 1
                if move == N*M:
                    linelst.append(lst)
                    return linelst
        R -= 1
        dir += 1
        if dir == 1 or dir == 3:
            for _ in range(R,0,-1):
                if dir == 1:
                    i += 1
                else:
                    i -= 1
                lst.append(arr[i][j])
                move += 1
                if move == N*M:
                    linelst.append(lst)
                    return linelst
        C -= 1
        dir = (dir+1)%4
        if dir == 0:
            linelst.append(lst)

### 회전 시키는 함수
linelst = chk()
for i in range(len(linelst)):
    lines = linelst[i]
    length = len(lines)
    linelst[i] = lines[T%length:] + lines[:T%length]


def make():
    newarr = [[0]*M for _ in range(N)]
    move = 0
    R, C = N, M
    i, j = 0, -1
    dir = 0
    idx, jdx = 0, 0
    while R>0 or C>0:
        if dir == 0 or dir == 2:
            for _ in range(C,0,-1):
                if dir == 0:
                    j += 1
                else:
                    j -= 1
                newarr[i][j] = linelst[idx][jdx]
                move += 1
                jdx += 1
                if move == N*M:
                    return newarr
        R -= 1
        dir += 1
        if dir == 1 or dir == 3:
            for _ in range(R,0,-1):
                if dir == 1:
                    i += 1
                else:
                    i -= 1
                newarr[i][j] = linelst[idx][jdx]
                move += 1
                jdx += 1
                if move == N*M:
                    return newarr
        C -= 1
        dir = (dir+1)%4
        if dir == 0:
            idx += 1
            jdx = 0

for k in make():
    print(*k)