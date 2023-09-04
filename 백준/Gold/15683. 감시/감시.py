import sys
from copy import deepcopy
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().rstrip().split())
arr = []
cctvlst, cctv5 = [], []
caselst = []
empty = 0
for i in range(N):
    line = input().rstrip().split()
    for j in range(M):
        if line[j] == '0':
            empty += 1
        elif line[j] != '6':
            if line[j] == '5': ### 무조건 다 살펴보는 CCTV
                cctv5.append((i,j))
            else:
                cctvlst.append((i,j, line[j]))
                if line[j] == '2':
                    caselst.append(2)
                else:
                    caselst.append(4)
    arr.append(line)
for ci,cj in cctv5:
    for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
        k = 1
        while True:
            ni, nj = ci+di*k, cj+dj*k
            if 0<=ni<N and 0<=nj<M:
                if arr[ni][nj] == '0':
                    arr[ni][nj] = '#'
                    empty -= 1
                elif arr[ni][nj] == '6':
                    break
                k += 1
            else:
                break
### CCTV 경우의 수 구하기
allcase = []
def dfs(n, case):
    if n == len(cctvlst):
        allcase.append(case)
        return
    for i in range(caselst[n]):
        dfs(n+1,case+[i])
dfs(0,[])
### 경우의 수마다 사각지대 갯수 구하기
cctvdict = {'1':[[(0,1)],[(1,0)],[(-1,0)],[(0,-1)]],
            '2':[[(0,-1),(0,1)], [(-1,0),(1,0)]],
            '3':[[(0,1),(-1,0)], [(0,1),(1,0)], [(0,-1),(1,0)], [(0,-1),(-1,0)]],
            '4':[[(0,-1),(1,0),(-1,0)], [(0,1),(1,0),(-1,0)], [(0,1),(0,-1),(-1,0)], [(0,1),(0,-1),(1,0)]]}
answer = N*M
for case in allcase:
    newarr = deepcopy(arr)
    cnt = empty
    for idx in range(len(case)):
        cctv_i, cctv_j, cctv_num = cctvlst[idx]
        for di, dj in cctvdict[cctv_num][case[idx]]:
            k = 1
            while True:
                ni, nj = cctv_i + di * k, cctv_j + dj * k
                if 0 <= ni < N and 0 <= nj < M:
                    if newarr[ni][nj] == '0':
                        newarr[ni][nj] = '#'
                        cnt -= 1
                    elif newarr[ni][nj] == '6':
                        break
                    k += 1
                else:
                    break

    answer = min(cnt, answer)
print(answer)