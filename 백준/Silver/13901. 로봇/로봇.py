import sys
input = sys.stdin.readline
R, C = map(int, input().split())
K = int(input())
arr = [[0]*C for _ in range(R)]
for _ in range(K):
    a, b = map(int, input().split())
    arr[a][b] = 1
si, sj = map(int, input().split())
arr[si][sj] = 1
orderlst = list(map(lambda x: int(x)-1, input().split()))
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]
answer = []
def solve():
    global si, sj
    dirset = set()
    pos = 0
    while True:
        dirset.add(orderlst[pos])
        di, dj = dirlst[orderlst[pos]]
        ni, nj = si+di, sj+dj
        if ni<0 or ni>=R or nj<0 or nj>=C or arr[ni][nj] == 1:
            pos = (pos+1)%4
            if orderlst[pos] in dirset:
                print(si,sj)
                return
            else: continue
        else:
            dirset = set()
            arr[ni][nj] = 1
            si, sj = ni, nj

solve()