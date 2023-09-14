import sys
from collections import deque
input = sys.stdin.readline
### 백조를 확인하면서 다음에 확인할 백조 리스트를 생성하는 함수
def check_goose(arr, visited, goose):
    nextlst = deque()
    while goose:
        gi, gj = goose.popleft()
        if gi == ei and gj == ej:
            return True, None

        for di, dj in [(0,1), (0,-1), (1,0), (-1,0)]:
            ni, nj = gi+di, gj+dj
            if 0<=ni<R and 0<=nj<C and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                if arr[ni][nj] == 'X':
                    nextlst.append((ni, nj))
                else:
                    goose.append((ni, nj))
    return False, nextlst

### 입력 받기
R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
gooselst = []
water = deque()
# for l in arr:
#     print(l)
for i in range(R):
    for j in range(C):
        if arr[i][j] != 'X':
            water.append((i,j))
            if arr[i][j] == 'L':
                gooselst.append((i,j))

visited = [[0]*C for _ in range(R)]

si, sj = gooselst[0]
ei, ej = gooselst[1]

day = 0
goose = deque()
goose.append((si,sj))
visited[si][sj] = 1
while True:
    ### 백조 만날 수 있는지 확인하고 안되면 다음 조회할 리스트 가져오기
    found, nextgoose = check_goose(arr, visited, goose)
    if found:
        break
    ### 얼음 녹이기 진행하면서 다음에 녹일 얼음 리스트 갱신하기
    for _ in range(len(water)):
        wi, wj = water.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = wi + di, wj + dj
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 'X':
                water.append((ni, nj))
                arr[ni][nj] = '.'
    goose = nextgoose
    day += 1

print(day)