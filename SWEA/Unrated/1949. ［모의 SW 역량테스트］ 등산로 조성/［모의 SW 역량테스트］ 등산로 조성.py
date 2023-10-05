from collections import deque

T = int(input())
def bfs(si, sj, arr):
    q = deque()
    q.append((si,sj))
    length = 0
    while q:
        length += 1
        for _ in range(len(q)):
            ci, cj = q.popleft()
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = ci+di, cj+dj
                if 0<=ni<N and 0<=nj<N and arr[ni][nj] < arr[ci][cj]:
                    q.append((ni,nj))

    return length

for tc in range(1, T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ### 높은 봉우리 찾기
    height, highest = 0, []
    for i in range(N):
        for j in range(N):
            if arr[i][j]>height: height, highest = arr[i][j], [(i,j)]
            elif arr[i][j] == height: highest.append((i,j))
    answer = 0
    for si, sj in highest:
        for ki in range(N):
            for kj in range(N):
                for k in range(1, K+1):
                    arr[ki][kj] -= k
                    length = bfs(si,sj,arr)
                    answer = max(answer, length)
                    arr[ki][kj] += k
    print(f"#{tc} {answer}")