import sys
input = sys.stdin.readline
sys.setrecursionlimit(10000)
N = int(input().rstrip())
arr = [[0]*N for _ in range(N)]
K = int(input().rstrip())
for _ in range(K):
    x, y = map(int, input().rstrip().split())
    arr[x-1][y-1] = 1
L = int(input().rstrip())
changedic = {}
for _ in range(L):
    a, b = input().rstrip().split()
    changedic[int(a)] = b

Dlst = [2,3,1,0]
Llst = [3,2,0,1]
# 동 서 남 북
dirlst = [(0,1), (0,-1), (1,0), (-1,0)]

def dfs(i, j, step, dir, lst):
    # print(i,j,step,dir,lst)
    di, dj = dirlst[dir]
    ni, nj = i+di, j+dj
    if 0>ni or ni>=N or 0>nj or nj>=N or (ni,nj) in lst:
        print(step+1)
        return
    if arr[ni][nj] == 1:
        arr[ni][nj] = 0
        if step+1 in changedic:
            if changedic[step+1] == 'D':
                dfs(ni,nj,step+1,Dlst[dir],lst+[(ni,nj)])
            else:
                dfs(ni, nj, step + 1, Llst[dir], lst + [(ni, nj)])
        else:
            dfs(ni, nj, step + 1, dir, lst + [(ni, nj)])
    else:
        if step+1 in changedic:
            if changedic[step+1] == 'D':
                dfs(ni,nj,step+1,Dlst[dir],lst[1:]+[(ni,nj)])
            else:
                dfs(ni, nj, step + 1, Llst[dir], lst[1:] + [(ni, nj)])
        else:
            dfs(ni, nj, step + 1, dir, lst[1:] + [(ni, nj)])
step, dir, i, j, lst = 0, 0, 0, 0, [(0,0)]
dfs(i, j, step, dir, lst)
