import sys
input = sys.stdin.readline
R, C, K = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(3)]

def solve():
    global arr
    rownum, colnum = 3, 3
    for time in range(100):
        if 0<=R-1<rownum and 0<=C-1<colnum and arr[R-1][C-1] == K:
            return time
        if rownum >= colnum:
            maxcol = 0
            newarr = []
            for idx in range(rownum):
                numdic = {}
                for num in arr[idx]:
                    if num == 0: continue
                    try: numdic[num] += 1
                    except: numdic[num] = 1
                newlst = [x for y in sorted(numdic.items(), key=lambda x: (x[1],x[0])) for x in y]
                newarr.append(newlst)
                maxcol = max(maxcol, len(newlst))

            if maxcol > 100: maxcol = 100
            for idx in range(rownum):
                if len(newarr[idx]) > maxcol:
                    newarr[idx] = newarr[idx][:maxcol]
                else:
                    newarr[idx] += [0] * (maxcol-len(newarr[idx]))
            colnum = maxcol
        else:
            arr_T = list(map(list, zip(*arr)))
            maxrow = 0
            newarr = []
            for jdx in range(colnum):
                numdic = {}
                for num in arr_T[jdx]:
                    if num == 0: continue
                    try: numdic[num] += 1
                    except: numdic[num] = 1
                newlst = [x for y in sorted(numdic.items(), key=lambda x: (x[1], x[0])) for x in y]
                newarr.append(newlst)
                maxrow = max(maxrow, len(newlst))

            if maxrow > 100: maxrow = 100
            for jdx in range(colnum):
                if len(newarr[jdx]) > maxrow:
                    newarr[jdx] = newarr[jdx][:maxrow]
                else:
                    newarr[jdx] += [0] * (maxrow-len(newarr[jdx]))
            rownum = maxrow
            newarr = list(map(list, zip(*newarr)))
        arr = newarr

    if 0 <= R - 1 < rownum and 0 <= C - 1 < colnum and arr[R - 1][C - 1] == K:
        return 100
    return -1
print(solve())