import sys
sys.setrecursionlimit(10000)
N = int(input())
arr = []
for _ in range(N):
    arr.append(input())
## 정상인이 보는 그림
graph1 = {}
visit1 = [[0]*N for _ in range(N)]
## 적록색약이 보는 그림
graph2 = {}
visit2 = [[0]*N for _ in range(N)]
for i in range(N):
    for j in range(N):
        color = arr[i][j]
        graph1[str(i) + '*' + str(j)] = []
        graph2[str(i) + '*' + str(j)] = []
        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = i+di, j+dj
            if 0<=ni<N and 0<=nj<N:
                if arr[ni][nj]==color:
                    graph1[str(i) + '*' + str(j)].append([ni,nj])
                    graph2[str(i) + '*' + str(j)].append([ni,nj])
                    # if str(ni)+'*'+str(nj) in graph1:
                    #     graph1[str(ni)+'*'+str(nj)].append([i, j])
                    # else:
                    #     graph1[str(ni)+'*'+str(nj)] = [[i,j]]
                    # if str(ni)+'*'+str(nj) in graph2:
                    #     graph2[str(ni)+'*'+str(nj)].append([i, j])
                    # else:
                    #     graph2[str(ni)+'*'+str(nj)] = [[i,j]]
                else:
                    if color!='B' and arr[ni][nj] != 'B':
                        graph2[str(i) + '*' + str(j)].append([ni, nj])
                        # if str(ni) + '*' + str(nj) in graph2:
                        #     graph2[str(ni) + '*' + str(nj)].append([i, j])
                        # else:
                        #     graph2[str(ni) + '*' + str(nj)] = [[i, j]]

def dfs1(node):
    ni, nj = node[0], node[1]
    visit1[ni][nj] = 1
    for n in graph1[str(ni)+'*'+str(nj)]:
        if visit1[n[0]][n[1]] != 1:
            dfs1(n)
def dfs2(node):
    ni, nj = node[0], node[1]
    visit2[ni][nj] = 1
    for n in graph2[str(ni) + '*' + str(nj)]:
        if visit2[n[0]][n[1]] != 1:
            dfs2(n)

cnt1, cnt2 = 0, 0
for i in range(N):
    for j in range(N):
        if visit1[i][j] != 1:
            cnt1 += 1
            dfs1([i,j])
        if visit2[i][j] != 1:
            cnt2 += 1
            dfs2([i,j])

print(cnt1, cnt2)