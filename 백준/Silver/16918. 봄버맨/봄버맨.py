import sys
input = sys.stdin.readline
R, C, N = map(int, input().rstrip().split())
arr = [list(input().rstrip()) for _ in range(R)]
lst = []
for s in range(2, N+1):
    if s%2==0:
        lst = []
        for i in range(R):
            for j in range(C):
                if arr[i][j] == '.':
                    arr[i][j] = 'O'
                else:
                    lst.append((i,j))
    else:
        for i, j in lst:
            arr[i][j] = '.'
            for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<R and 0<=nj<C:
                    arr[ni][nj] = '.'

for l in arr:
    print(''.join(l))