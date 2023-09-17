import sys, heapq
from collections import deque
input = sys.stdin.readline
### 입력받기
N, M = map(int, input().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

visited = [[0]*M for _ in range(N)]

### 섬의 갯수 찾기 및 섬별 외곽 리스트 생성
cnt = 0
outlinelst = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1 and visited[i][j] == 0:
            cnt += 1
            outline = set()
            q = deque()
            q.append((i,j))
            visited[i][j] = cnt ### 방문처리 동시에 몇번째 섬인지 등록
            while q:
                ci, cj = q.popleft()
                for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                    ni, nj = ci+di, cj+dj
                    if 0<=ni<N and 0<=nj<M:
                        if arr[ni][nj] == 1 and visited[ni][nj] == 0:
                            q.append((ni,nj))
                            visited[ni][nj] = cnt
                        elif arr[ni][nj] == 0:
                            outline.add((ci,cj,di,dj)) ### 외곽 라인 추가 및 어느 방향으로 외곽인지
            outlinelst.append(outline)

# print(outlinelst)
### 섬별 최소 거리 만들기
graph = {i:[max(N,M)]*(cnt+1) for i in range(1, cnt+1)}
for num in range(cnt):
    for si, sj, di, dj in outlinelst[num]: ### num+1번 섬의 외곽리스트
        k = 1
        while True:
            ni, nj = si+di*k, sj+dj*k
            if ni<0 or ni>=N or nj<0 or nj>=M: break ### 벗어나면
            if 0<=ni<N and 0<=nj<M and visited[ni][nj] != 0: ### 가다가 섬을 만나면
                islandnum = visited[ni][nj]
                if k-1>=2:
                    graph[num+1][islandnum] = min(graph[num+1][islandnum], k-1)
                break
            k += 1
distgraph = {}
for i in range(1, cnt+1):
    lst = []
    for c in range(1, cnt+1):
        if c==i: continue
        if graph[i][c] != max(N,M):
            lst.append((c,graph[i][c]))
    distgraph[i] = lst

def prim(s):
    q = [(0, s)]
    mst = [0] * (cnt + 1)
    ans = 0

    while q:  # q에 데이터가 있는 동안
        w, c = heapq.heappop(q)
        if mst[c] == 0:  # 가장작은 MST에 포함안된 노드를 찾음
            mst[c] = 1
            ans += w

            for n, w in distgraph[c]:  # 현재 노드에서 연결된 노드를 찾아서 큐에 넣음
                if mst[n] == 0:
                    heapq.heappush(q, (w, n))
    if sum(mst) == cnt:
        return ans
    return -1
print(prim(1))