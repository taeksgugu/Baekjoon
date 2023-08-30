import sys
from collections import deque
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = [list(input().rstrip().split()) for _ in range(N)]
cnt = [x for y in arr for x in y].count('1') ### 총 치즈수 파악
beforecnt = cnt
def solve():
    global cnt,beforecnt
    time = 1
    while cnt > 0: ## 치즈수가 0이 되기 전까지 시간 보내기
        beforecnt = cnt ## 이전 치즈수 업데이트
        q = deque()
        q.append((0,0))
        visited = [[0]*M for _ in range(N)] ### 방문처리할 리스트 생성
        visited[0][0] = 1
        while q:
            i, j = q.popleft()
            for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
                ni, nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                    if arr[ni][nj] == '1': ### 이번 시간에 녹는 치즈
                        arr[ni][nj] = '0'
                        cnt -= 1 ### 치즈수 업데이트
                    else:
                        q.append((ni,nj))
                    visited[ni][nj] = 1
        time += 1
    print(time-1)
    print(beforecnt)
    return
solve()