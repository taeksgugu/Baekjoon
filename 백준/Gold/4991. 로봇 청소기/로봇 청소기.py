import sys
from  collections import deque
input = sys.stdin.readline

def bfs(si,sj,ei,ej):
    visited = [[-1]*W for _ in range(H)]
    q = deque()
    q.append((si,sj))
    visited[si][sj] = 0
    while q:
        ci, cj = q.popleft()
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<H and 0<=nj<W and arr[ni][nj] != 'x' and visited[ni][nj] == -1:
                if ni==ei and nj==ej: return True, visited[ci][cj]+1
                visited[ni][nj] = visited[ci][cj] + 1
                q.append((ni,nj))
    return False, -1
while True:
    W, H = map(int, input().split())
    if W==0 and H==0: break
    arr = [list(input().rstrip()) for _ in range(H)]
    dirtylst = []
    for i in range(H):
        for j in range(W):
            if arr[i][j] == 'o': si, sj = i, j
            elif arr[i][j] == '*': dirtylst.append((i,j))
    answer = 1e9
    dirtycnt = len(dirtylst)

    ### 시작점, 더러운 지점들 간의 거리 및 갈 수 있는 여부 확인
    ### 애초에 못가면 더 진행할 필요도 없음
    chklst = [(si,sj)] + dirtylst
    distdict = {}
    flag = False
    for i in range(dirtycnt+1):
        for j in range(i+1, dirtycnt+1):
            ai,aj = chklst[i]
            bi,bj = chklst[j]
            can, dist = bfs(ai,aj,bi,bj)
            # print(ai, aj, bi, bj, can, dist)
            if can:
                distdict[(ai,aj,bi,bj)] = dist
                distdict[(bi,bj,ai,aj)] = dist
            else:
                print(-1)
                flag = True
                break
        if flag:
            break

    if not flag:
        v = [0]*dirtycnt
        def robot(n, si,sj,dist):
            global answer, flag
            if n == dirtycnt:
                answer = min(dist, answer)
                return
            if dist >= answer: return
            for idx in range(dirtycnt):
                if v[idx] == 0:
                    ei, ej = dirtylst[idx]
                    newdist = distdict[(si,sj,ei,ej)]
                    v[idx] = 1
                    robot(n+1, ei, ej, dist+newdist)
                    v[idx] = 0

        robot(0,si,sj,0)
        if answer == 1e9: print(-1)
        else: print(answer)