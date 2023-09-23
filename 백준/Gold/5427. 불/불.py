import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    arr = [list(input().rstrip()) for _ in range(H)]
    totalcnt, firecnt = W*H, 0
    fireq, q = deque(), deque() ### 불, 상근
    visited = [[0]*W for _ in range(H)] ### 상근이 방문처리
    for i in range(H):
        for j in range(W):
            if arr[i][j] == '#': totalcnt -= 1
            elif arr[i][j] == '*':
                firecnt += 1
                fireq.append((i,j))
            elif arr[i][j] == '@':
                arr[i][j] = '.' ## 빈공간으로 바꿔놓기
                q.append((i,j))
                visited[i][j] = 1

    def solve():
        global firecnt
        time = 1
        while True: ### 시간은 흘러간다
            ### 불부터 이동
            if fireq:
                # print(fireq)
                for _ in range(len(fireq)):
                    fi, fj = fireq.popleft()
                    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                        ni,nj = fi+di, fj+dj
                        if 0<=ni<H and 0<=nj<W and arr[ni][nj] == '.': ### 빈공간이면 퍼지자
                            arr[ni][nj] = '*'
                            firecnt += 1 ### 불난 칸 + 1
                            fireq.append((ni,nj))



            ### 상근이 이동
            for _ in range(len(q)):
                si, sj = q.popleft()
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    ni,nj = si+di, sj+dj
                    if ni<0 or ni>=H or nj<0 or nj>=W: return time ### 탈출 성공
                    if 0<=ni<H and 0<=nj<W and arr[ni][nj] == '.' and visited[ni][nj] == 0: ### 빈공간으로 도망
                        visited[ni][nj] = 1
                        q.append((ni,nj))


            if not q or firecnt == totalcnt:  ### 상근이가 갈 곳이 없다면 or 모든 칸 불태웠으면
                return 'IMPOSSIBLE'
            ### 시간 추가
            time += 1

    print(solve())
