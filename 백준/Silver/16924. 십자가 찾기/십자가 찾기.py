import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
star = []
arr = []
answer = 0
anslst = []
visited = [[0] * M for _ in range(N)]
for i in range(N):
    lst = list(input().rstrip())
    cnt = 0
    for j in range(M):
        if lst[j] == '*':
            arr.append([i,j])
            visited[i][j] = 1
    star.append(lst)
def makecross(x,y):
    global answer
    k = 1
    go = True
    while go:
        for di, dj in [(-1,0), (0,1), (1,0),(0,-1)]:
            ni, nj = x+di*k, y+dj*k
            if 0<=ni<N and 0<=nj<M and star[ni][nj] == '*':
                continue
            else:
                go = False
                break
        else:
            k += 1
    # print(k-1)
    answer += (k-1)
    visited[x][y] = 0
    for idx in range(k-1,0,-1):
        anslst.append([x+1,y+1,idx])
        for di, dj in [(-1,0), (0,1), (1,0),(0,-1)]:
            ni, nj = x+di*idx, y+dj*idx
            visited[ni][nj] = 0

def cross(arr):
    global answer
    for point in arr:
        i, j = point
        for di, dj in [(-1,0), (0,1), (1,0),(0,-1)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<M and star[ni][nj] == '*':
                continue
            else:
                break
        else:
            # print(i,j)
            makecross(i,j)

cross(arr)

if 1 in [x for y in visited for x in y]:
    print(-1)
else:
    print(answer)
    for ans in anslst:
        print(*ans)