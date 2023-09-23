import sys,heapq
input = sys.stdin.readline
N = int(input().rstrip())
favor = {}
for _ in range(N*N):
    lst = list(map(int, input().rstrip().split()))
    favor[lst[0]] = lst[1:]
visited = [[[0,0] for _ in range(N)] for _ in range(N)]
# print(favor)
for student, favorites in favor.items():
    seatlst = []
    for i in range(N):
        for j in range(N):
            if visited[i][j][0] == 0:
                lovers = 0
                empty = 0
                favorlst = []
                for di, dj in [(0,1),(0,-1), (1,0),(-1,0)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N:
                        if visited[ni][nj][0] == 0:
                            empty -= 1
                        elif visited[ni][nj][0] in favorites:
                            lovers -= 1
                        if visited[ni][nj][0] != 0 and student in favor[visited[ni][nj][0]]:
                            favorlst.append((ni,nj))
                heapq.heappush(seatlst,(lovers,empty,i,j,favorlst))
    l, e, a, b, f_lst = heapq.heappop(seatlst)
    visited[a][b][0] = student
    visited[a][b][1] = l*(-1)
    for ki, kj in f_lst:
        visited[ki][kj][1] += 1

    # # print(student, lovers)
    # for l in visited:
    #     print(l)
answer = 0
satisfylst = [0,1,10,100,1000]
for i in range(N):
    for j in range(N):
        answer += satisfylst[visited[i][j][1]]
print(answer)