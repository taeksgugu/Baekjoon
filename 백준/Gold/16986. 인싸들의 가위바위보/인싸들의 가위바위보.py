import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]
kyunghee = list(map(lambda x:int(x)-1, input().rstrip().split()))
minho = list(map(lambda x:int(x)-1, input().rstrip().split()))

def game(lst):
    wincnt, khcnt, mhcnt = 0, 0, 0
    case = 0 ## 0: 지우, 경희 / 1: 경희, 민호 / 2: 지우, 민호
    khlst = kyunghee[:]
    mhlst = minho[:]
    while lst:
        if case == 0:
            jw, kh = lst.pop(0), khlst.pop(0)
            if arr[jw][kh] != '2':
                khcnt += 1
                case = 1
            else:
                wincnt += 1
                case = 2
        elif case == 1:
            mh, kh = mhlst.pop(0), khlst.pop(0)
            if arr[kh][mh] != '2':
                mhcnt += 1
                case = 2
            else:
                khcnt += 1
                case = 0
        else:
            jw, mh = lst.pop(0), mhlst.pop(0)
            if arr[jw][mh] != '2':
                mhcnt += 1
                case = 1
            else:
                wincnt += 1
                case = 0
        if khcnt == K or mhcnt == K:
            return False
        if wincnt == K:
            return True
    return False

v = [0] * N
answer = 0
def makecomb(n, lst):
    global answer
    if answer == 1:
        return
    if n == N:
        if game(lst):
            answer = 1
        return
    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            makecomb(n+1, lst+[i])
            v[i] = 0
makecomb(0,[])
print(answer)