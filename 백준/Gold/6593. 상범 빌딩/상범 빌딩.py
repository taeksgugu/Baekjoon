import sys
from collections import deque
input = sys.stdin.readline


while True:
    L, R, C = map(int, input().split())
    if L == 0 and R == 0 and C == 0: break
    start, end = False, False
    arr = []
    for floornum in range(L):
        floor = [list(input().rstrip()) for _ in range(R)]
        _ = input() ### 빈칸 넘기기
        if not start or not end: ### 둘 중 하나라도 찾아야한다면
            for i in range(R):
                for j in range(C):
                    if floor[i][j] == 'S':
                        sl, si, sj = floornum, i, j
                        floor[i][j] = '.'
                        start =True
                    elif floor[i][j] == 'E':
                        el, ei, ej = floornum, i, j
                        floor[i][j] = '.'
                        end = True
        arr.append(floor)

    ### 디버깅
    # print(sl,si,sj, el,ei,ej)

    def bfs():
        visited = [[[0]*C for _ in range(R)] for _ in range(L)]
        q = deque()
        q.append((sl, si, sj))
        visited[sl][si][sj] = 1

        while q:
            cl, ci, cj = q.popleft()
            for dl, di, dj in [(0,0,1), (0,0,-1), (0,1,0), (0,-1,0), (-1,0,0), (1,0,0)]: # 동,서,남,북,상,하
                nl, ni, nj = cl+dl, ci+di, cj+dj
                if 0<=nl<L and 0<=ni<R and 0<=nj<C and arr[nl][ni][nj] == '.' and visited[nl][ni][nj] == 0:
                    if nl==el and ni==ei and nj==ej:
                        return f'Escaped in {visited[cl][ci][cj]} minute(s).'
                    visited[nl][ni][nj] = visited[cl][ci][cj] + 1
                    q.append((nl, ni, nj))

        return 'Trapped!'

    print(bfs())