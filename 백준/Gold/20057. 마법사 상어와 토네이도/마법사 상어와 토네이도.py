import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
start = [(N-1)//2, (N-1)//2]
visited = [[0]*N for _ in range(N)]
### 토네이도 도는 방향 리스트 및 모래 퍼짐 고려 리스트 생성
direction = []
for k in range(1,N,2):
    lst = [0]*k + [1]*k + [2]*(k+1) + [3]*(k+1)
    direction += lst
direction += [0]*(N-1)

dirlst = [(0,-1), (1,0), (0,1), (-1,0)] ## 토네이도 방향 -> 좌 하 우 상
effect = [[(-1,0,1), (1,0,1), (-2,-1,2), (2,-1,2), (-1,-1,7), (1,-1,7), (-1,-2,10), (1,-2,10), (0,-3, 5)], ### 좌
         [(0,-1,1), (0,1,1), (1,-2,2), (1,2,2), (1,-1,7), (1,1,7), (2,-1,10), (2,1,10), (3,0, 5)], ### 하
         [(-1,0,1), (1,0,1), (-2,1,2), (2,1,2), (-1,1,7), (1,1,7), (-1,2,10), (1,2,10), (0,3, 5)], ### 우
         [(0,-1,1), (0,1,1), (-1,-2,2), (-1,2,2), (-1,-1,7), (-1,1,7), (-2,-1,10), (-2,1,10), (-3,0, 5)] ### 상
]
cnt = 1
i, j = start
answer = 0
for dir in direction:
    di, dj = dirlst[dir]
    ni, nj = i+di, j+dj
    ki, kj = i+di*2, j+dj*2
    sand = arr[ni][nj]
    remains = sand
    arr[ni][nj] = 0
    for ci, cj,rate in effect[dir]:
        oi, oj = i+ci, j+cj
        if 0<=oi<N and 0<=oj<N:
            arr[oi][oj] += sand*rate//100
        else:
            answer += sand*rate//100
        remains -= sand*rate//100


    if 0 <= ki < N and 0 <= kj < N:
        arr[ki][kj] += remains
    else:
        answer += remains
    i, j = ni, nj
print(answer)
