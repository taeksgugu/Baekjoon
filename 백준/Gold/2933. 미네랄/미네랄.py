import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
L = int(input())
orderlst = list(map(int, input().rstrip().split()))
def gravity(arr):
    visited = [[0]*M for _ in range(N)]
    grouplst = []
    newarr = [['.']*M for _ in range(N)]
    for i in range(N-1, -1, -1):
        for j in range(M):
            if visited[i][j] == 0 and arr[i][j] == 'x':
                group = [(i,j)]
                visited[i][j] = 1
                q = deque()
                q.append((i,j))
                while q:
                    ci, cj = q.popleft()
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni, nj = ci+di, cj+dj
                        if 0<=ni<N and 0<=nj<M and arr[ni][nj]=='x' and visited[ni][nj] == 0:
                            visited[ni][nj] = 1
                            q.append((ni,nj))
                            group.append((ni,nj))
                if i==N-1: ### 처음부터 밑에 있었다면
                    for gi, gj in group:
                        newarr[gi][gj] = 'x'
                else: grouplst.append(group)

    for group in grouplst:
        level, flag = 1, False
        while not flag:
            for ci, cj in group:
                if ci+level>=N or newarr[ci+level][cj] != '.':
                    flag=True
                    break
            else:
                level += 1
        for gi, gj in group:
            newarr[gi+level-1][gj] = 'x'
    return newarr

# for l in gravity(arr):
#     print(*l)

for idx in range(L):
    rownum = N-orderlst[idx]
    if idx%2==0: ### 왼쪽에서
        for j in range(M):
            if arr[rownum][j] == 'x':
                arr[rownum][j] = '.'
                break
    else:
        for j in range(M-1,-1,-1):
            if arr[rownum][j] == 'x':
                arr[rownum][j] = '.'
                break

    arr = gravity(arr)

    ### 디버깅
    # for l in arr:
    #     print(*l)
    # print()
for l in arr:
    print(''.join(l))