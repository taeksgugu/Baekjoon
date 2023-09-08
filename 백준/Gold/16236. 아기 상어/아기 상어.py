### 1차 개선 -> findfish에 거리를 추가하지 않고 바로 return하는 방식으로 시간 단축 시도
import sys
from collections import deque
input = sys.stdin.readline

### 물고기와 상어의 거리를 구하는 함수 (맨해튼 거리가 아니라 중간에 사이즈가 크거나 같은 물고기 고려)
def sharkfind(baby_i, baby_j):
    q = deque()
    visited = [[-1]*N for _ in range(N)]
    q.append((baby_i, baby_j))
    visited[baby_i][baby_j] = 0
    dist = 1
    findfish = []
    while q:
        for _ in range(len(q)):
            i, j = q.popleft()
            for di, dj in [(-1,0), (0,-1), (0,1), (1,0)]:
                ni,nj = i+di, j+dj
                if 0<=ni<N and 0<=nj<N and visited[ni][nj] == -1 and arr[ni][nj] <= size:
                    if arr[ni][nj] < size and (ni,nj) in fishlst:
                        findfish.append((ni,nj))
                    else:
                        q.append((ni,nj))
                    visited[ni][nj] = dist
        if not findfish: ### 한번돌 때 찾은 물고기가 없다면 계속 진행
            dist += 1
        else:
            return sorted(findfish), dist
    return sorted(findfish), 0
### 전체 함수
def solve():
    global baby_i,baby_j, size
    ### 변수 설정 (초기 아기 상어 크기 & 크기 커지기 전 먹은 물고기 수 & 시간)
    size, cnt, time = 2, 0, 0
    while True: ## 물고기 리스트에 아기 상어보다 작은 물고기가 없을 때까지
        turnlst, distance = sharkfind(baby_i,baby_j) ### 해당 턴에 아기 상어가 물고기를 찾음
        if turnlst:
            ### 젤 가깝고 가장 위, 가장 왼쪽 물고기 먹음
            fish_i, fish_j = turnlst[0]
            arr[baby_i][baby_j] = 0
            baby_i, baby_j = fish_i, fish_j
            time += distance
            cnt += 1
            fishlst.remove((fish_i,fish_j))
            ### 해당 물고기 있던 칸은 아기 상어가 감
            arr[fish_i][fish_j] = 9

            if cnt == size: ### 아기 상어 크기만큼 먹어서 크기 추가 및 물고기수 초기화
                size += 1
                cnt = 0
        else:
            return time

N = int(input().strip())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
fishlst = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 9: baby_i, baby_j = i, j
        elif arr[i][j] != 0:
            fishlst.append((i,j)) ### fishlst sort 필요 없음 순서대로 넣어서

print(solve())