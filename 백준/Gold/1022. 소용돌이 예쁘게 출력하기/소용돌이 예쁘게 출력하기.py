import sys
input = sys.stdin.readline
r1, c1, r2, c2 = map(int, input().split())
dirlst = [(0,1), (-1,0), (0,-1), (1,0)]
def snail():
    arr = [[0]*(c2-c1+1) for _ in range(r2-r1+1)]
    total = (c2-c1+1)*(r2-r1+1)
    si,sj = -r1, -c1
    maxlen = 0
    if 0<=si<r2-r1+1 and 0<=sj<c2-c1+1:
        arr[si][sj] = 1
        total -= 1
    idx, d, cnt, flag, length = 2, 0, 0, 0, 1
    while total>0:
        di, dj = dirlst[d]
        si, sj = si+di, sj+dj
        if 0<=si<r2-r1+1 and 0<=sj<c2-c1+1:
            arr[si][sj] = idx
            total-=1
            maxlen = max(maxlen, len(str(idx)))
        cnt += 1
        idx += 1
        if cnt == length:
            d = (d+1) % 4
            cnt = 0
            if flag == 0: flag = 1
            else:
                flag = 0
                length += 1
    return arr, maxlen

arr, length = snail()
for i in range(r2-r1+1):
    for j in range(c2-c1+1):
        print(str(arr[i][j]).rjust(length), end=" ")
    print()