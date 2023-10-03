import sys
from collections import deque
input = sys.stdin.readline

R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
orderlst = list(map(int, list(input().rstrip())))

dirlst = {1:(1,-1), 2:(1,0), 3:(1,1), 4:(0,-1), 5:(0,0), 6:(0,1), 7:(-1,-1), 8:(-1,0), 9:(-1,1)}
crazydir = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
def solve():
    ### 종수 아두이노와 미친 아두이노 좌표 구하기
    crazylst = []
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'I':
                si, sj = i, j
                arr[i][j] = '.'
            elif arr[i][j] == 'R':
                crazylst.append((i,j))
                arr[i][j] = '.'

    for roundnum in range(len(orderlst)):
        ### 종수 아두이노 이동
        di, dj = dirlst[orderlst[roundnum]]
        si, sj = si+di, sj+dj

        ### 보드를 벗어나는 입력은 주어지지 않기 때문에 해당 좌표에 미친 아두이노가 있는지만 확인하면 됨
        if (si,sj) in crazylst: ### 미친 아두이노 있는 좌표면
            return False, roundnum+1 ### 전까지 이동한 횟수

        ### 미친 아두이노 이동 시작
        newarr = [[[] for _ in range(C)] for _ in range(R)]
        for ci, cj in crazylst:
            movelst = []
            for di, dj in crazydir:
                ni, nj = ci+di, cj+dj
                if 0<=ni<R and 0<=nj<C:
                    dist = abs(ni-si) + abs(nj-sj)
                    movelst.append((dist, ni, nj))

            movelst.sort(key=lambda x: x[0]) ### 거리가 가장 작아지는순 정렬
            _, mi, mj = movelst[0]
            if mi == si and mj == sj: ### 종수가 이동한 칸이라면
                return False, roundnum+1
            newarr[mi][mj].append(1)

        ### 이동한 후 새로운 미친 아두이노 좌표 리스트 만들기
        newcrazy = []
        for i in range(R):
            for j in range(C):
                if len(newarr[i][j])==1: ### 딱 하나만 있을 때
                    newcrazy.append((i,j))

        crazylst = newcrazy

    ### 만약 무사히 다 지나갔다면
    answer = [['.']*C for _ in range(R)]
    answer[si][sj] = 'I'
    for ci, cj in crazylst:
        answer[ci][cj] = 'R'

    return True, answer

cango, answer = solve()
if cango:
    for l in answer:
        print(''.join(l))
else:
    print(f"kraj {answer}")