### 1차 시도 : 틀림 -> 테트로미노 좌표 입력 실수
### 2차 시도 : 틀림 -> 대칭 고려 x
### 3,4차 시도 대칭을 고려했지만 인덱스 번호를 고치지 않았음:
import sys
input = sys.stdin.readline
N, M = map(int,input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
# N, M = 500, 500
# arr = [[1]*500 for _ in range(500)]
tetromino = [[(0,1), (0,2), (0,3)],
    [(1,0), (2,0), (3,0)],
    [(0,1), (1,0), (1,1)],
    [(1,0), (2,0), (2,1)],
    [(0,1), (0,2), (1,0)],
    [(0,1), (1,1), (2,1)],
    [(0,1), (0,2), (-1,2)],
    [(1,0), (1,1), (2,1)],
    [(0,1), (-1,1), (-1,2)],
    [(-1,1), (0,1), (1,1)],
    [(0,1), (0,2), (-1,1)],
    [(1,0), (2,0), (1,1)],
    [(0,1), (0,2), (1,1)],
    [(0,1), (-1,1), (-2,1)],
    [(0,1), (0,2), (1,2)],
    [(0,1), (1,0), (2,0)],
    [(1,0), (1,1), (1,2)],
    [(1,0), (0,1), (-1,1)],
    [(0,1), (1,1), (1,2)]]

def cal(i,j, case):
    cnt = arr[i][j]
    for di, dj in case:
        ni, nj = i+di, j+dj
        if ni<0 or ni>=N or nj<0 or nj>=M: return 0
        # if 0<=ni<N and 0<=nj<M:
        cnt += arr[ni][nj]
    return cnt

answer = 0
for i in range(N):
    for j in range(M):
        for case in tetromino:
        # for idx in range(13):
        #     case = tetromino[idx]
            casecnt = cal(i,j,case)
            if casecnt > answer:
                answer = casecnt
print(answer)
