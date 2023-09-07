### 1차 시도 : 틀림 -> 테트로미노 좌표 입력 실수
### 2차 시도 : 틀림 -> 대칭 고려 x
### 3,4차 시도 대칭을 고려했지만 인덱스 번호를 고치지 않았음
import sys
input = sys.stdin.readline
N, M = map(int,input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

### 1번째 통과한 코드 : 모든 테트로미노를 구현하여 풀이한 경우
# tetromino = [[(0,1), (0,2), (0,3)],[(1,0), (2,0), (3,0)], [(0,1), (1,0), (1,1)],
#     [(1,0), (2,0), (2,1)], [(0,1), (0,2), (1,0)], [(0,1), (1,1), (2,1)], [(0,1), (0,2), (-1,2)],
#     [(1,0), (1,1), (2,1)], [(0,1), (-1,1), (-1,2)], [(-1,1), (0,1), (1,1)], [(0,1), (0,2), (-1,1)],
#     [(1,0), (2,0), (1,1)], [(0,1), (0,2), (1,1)], [(0,1), (-1,1), (-2,1)], [(0,1), (0,2), (1,2)],
#     [(0,1), (1,0), (2,0)], [(1,0), (1,1), (1,2)], [(1,0), (0,1), (-1,1)], [(0,1), (1,1), (1,2)]]
# 
# def cal(i,j, case):
#     cnt = arr[i][j]
#     for di, dj in case:
#         ni, nj = i+di, j+dj
#         if ni<0 or ni>=N or nj<0 or nj>=M: return 0
#         cnt += arr[ni][nj]
#     return cnt
# 
# answer = 0
# for i in range(N):
#     for j in range(M):
#         for case in tetromino:
#             casecnt = cal(i,j,case)
#             if casecnt > answer:
#                 answer = casecnt
# print(answer)

### 2번째 : 테트로미노를 다르게 생각하면 한 칸에서 4칸을 잇는 걸로 이전에 풀었던 칠공주와 비슷함
visited = [[0] * M for _ in range(N)] ### 바깥에 빼놓은 이유는 이번 DFS는 모든 경우에서 다시 한칸씩 들어가는 것이기 때문에
                                    ### 다른 지점에서 다시 그 칸을 방문하지 않게 하기 위함
maxnum = max([x for y in arr for x in y])
answer = 0
def dfs(n, lst, cnt):
    global answer
    if cnt + maxnum * (4 - n) <= answer:
        return
    if n == 4:
        answer = max(answer, cnt)
        return
    for ci, cj in lst:
        visited[ci][cj] = 1
        for di, dj in [(0, 1), (0, -1), (1, 0)]:
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < M and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                dfs(n + 1, lst + [(ni, nj)], cnt + arr[ni][nj])
                visited[ni][nj] = 0

for i in range(N):
    for j in range(M):
        dfs(1, [(i, j)], arr[i][j])
print(answer)