import sys
from collections import deque
input = sys.stdin.readline
N, M, G, R = map(int, input().rstrip().split())
arr = []
possiblearea = []
for i in range(N):
    line = input().rstrip().split()
    for j in range(M):
        if line[j] == '2':
            possiblearea.append((i,j))
    arr.append(line)

### 조합 만들기
comblst = []
def dfs(idx, green, red):
    if len(green) == G and len(red) == R:
        comblst.append((green,red))
        return
    if idx == len(possiblearea):
        return
    dfs(idx+1, green+[possiblearea[idx]], red)
    dfs(idx+1, green, red+[possiblearea[idx]])
    dfs(idx+1, green, red)
dfs(0,[],[])

### 꽃 수 계산
answer = 0
for green, red in comblst:
    flower = 0
    visited = [[-1]*M for _ in range(N)]
    for gi,gj in green:
        visited[gi][gj] = 0
    for ri,rj in red:
        visited[ri][rj] = 0
    gq = deque(green)
    rq = deque(red)
    while gq:
        for _ in range(len(gq)):
            gi, gj = gq.popleft()
            if visited[gi][gj] != 'F':
                visited[gi][gj] = 0
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ngi, ngj = gi+di, gj+dj
                    if 0<=ngi<N and 0<=ngj<M and arr[ngi][ngj] != '0' and visited[ngi][ngj] == -1:
                        visited[ngi][ngj] = 'G'
                        gq.append((ngi,ngj))
        for _ in range(len(rq)):
            ri, rj = rq.popleft()
            # visited[ri][rj] = 0
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                nri, nrj = ri+di, rj+dj
                if 0<=nri<N and 0<=nrj<M and arr[nri][nrj] != '0' and visited[nri][nrj] in [-1, 'G']:
                    if visited[nri][nrj] == -1:
                        visited[nri][nrj]= 0
                        rq.append((nri,nrj))
                    elif visited[nri][nrj] == 'G':
                        flower += 1
                        visited[nri][nrj] = 'F'
    answer = max(answer,flower)
print(answer)