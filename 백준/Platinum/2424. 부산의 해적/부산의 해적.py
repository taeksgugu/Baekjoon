import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
sq, pq = deque(), deque()
visited = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'Y':
            sq.append((i,j))
            visited[i][j] = 1
            arr[i][j] = '.'
        elif arr[i][j] == 'V':
            pq.append((i,j))

def check(si,sj):
    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
        k = 1
        while True:
            ni, nj = si+di*k, sj+dj*k
            if ni<0 or ni>=N or nj<0 or nj>=M: break
            if arr[ni][nj] == 'V': return False
            if arr[ni][nj] == 'I': break
            else: k += 1
    return True
def solve():
    while sq:
        ### 수아 이동
        for _ in range(len(sq)):
            si, sj = sq.popleft()
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = si+di, sj+dj
                if 0<=ni<N and 0<=nj<M and (arr[ni][nj] == '.' or arr[ni][nj] == 'T') and visited[ni][nj] == 0:
                    visited[ni][nj] = 1
                    sq.append((ni,nj))
                    # if arr[ni][nj] == 'T': return 'YES'

        ### 해적 이동
        for _ in range(len(pq)):
            pi, pj = pq.popleft()
            for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                ni, nj = pi+di, pj+dj
                if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '.':
                    arr[ni][nj] = 'V'
                    pq.append((ni,nj))

        ### 수아 생존 여부 확인
        for _ in range(len(sq)):
            si, sj = sq.popleft()
            if check(si, sj):
                sq.append((si,sj))
                if arr[si][sj] == 'T': return 'YES'
    return 'NO'

print(solve())