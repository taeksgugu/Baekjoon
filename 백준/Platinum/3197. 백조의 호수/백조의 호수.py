### 초기 풀이 과정: 처음에 문제를 읽고서는 돌면서 녹이고 조회할 생각을 했는데, R과 C의 범위를 보자마자 안되겠다고 판단
###              그 결과, 처음부터 각 얼음이 언제 녹을지를 파악하고, 한번에 BFS를 돌리면서 조회하는 걸 고려해봄
###              이 방식으로 3번의 시간초과와 1번의 오답이 발생함 / 내가 만든 테케로 시간 초과날 걸 알았지만 오기에 제출하긴 했음
###              R=1500, C=1500, arr[0][0] 이랑 arr[-1][-1]에 백조 위치하고 다 빙판일 경우를 돌려서 빠르게 된다면 시간 초과는 걱정 X
### 5차 시도 : 263012kb 1148ms
###         더 간결해야 한다고 생각했고 내가 만든 테케를 돌릴 때, 백조 만나는 것도 오래 걸리고 얼음 탐색도 생각보다 오래 걸리는게 보였음
###         arr을 다 순회하는게 문제라고 생각했고 이전에 다른 구현문제에서 풀었던 것처럼 리스트로 좌표를 관리하는 방식을 선정함
###         백조가 돌고 나서 다음 턴에 돌 백조 리스트를 돌면서 생성하고, 얼음도 녹으면서 다음에 녹을 얼음 리스트를 만들고 턴을 끝내면서 시간을 단축함
### 6차 시도 : 267080kb 1496ms
###         더 깔끔하게 간결하게 정리해봄, 변수명도 좀 더 이해하기 쉽게 ㅎㅎ
###         solve()함수로 정리했는데 확실히 느려짐. 함수 호출이 확실히 속도 저하가 있는 듯함
### 7차 시도 : 262072kb 1240ms
###         함수를 다 없애고, rstrip()을 짧은거 받을 때는 안 사용해보기로 함.(그냥 궁금증)
import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
R, C = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(R)]
visited = [[0]*C for _ in range(R)]
gooselst = []
meltlst = deque()
### 백조 좌표 구하기 및 초기 조회할 호수 리스트
for i in range(R):
    for j in range(C):
        if arr[i][j] != 'X':
            meltlst.append((i,j))
            if arr[i][j] == 'L':
                gooselst.append((i,j))

si, sj = gooselst[0] ### 백조 스타트 좌표
ei, ej = gooselst[1] ### 백조 끝나는 좌표
### 본격적으로 백조의 호수 진행하기
day = 0
goose = deque()
goose.append((si,sj))
visited[si][sj] = 1
found = False
while True:
    ### 백조 만날 수 있는지 확인하고 안되면 다음 조회할 리스트 가져오기
    nextgoose= deque()
    while goose:
        gi, gj = goose.popleft()
        if gi == ei and gj == ej:
            found = True
            break
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = gi + di, gj + dj
            if 0 <= ni < R and 0 <= nj < C and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                if arr[ni][nj] == 'X':
                    nextgoose.append((ni, nj))
                else:
                    goose.append((ni, nj))
    goose = nextgoose
    if found: break
    ### 얼음 녹이기 진행하면서 다음에 녹일 얼음 리스트 갱신하기
    for _ in range(len(meltlst)):
        wi, wj = meltlst.popleft()
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            ni, nj = wi + di, wj + dj
            if 0 <= ni < R and 0 <= nj < C and arr[ni][nj] == 'X':
                meltlst.append((ni, nj))
                arr[ni][nj] = '.'
    day += 1
print(day)