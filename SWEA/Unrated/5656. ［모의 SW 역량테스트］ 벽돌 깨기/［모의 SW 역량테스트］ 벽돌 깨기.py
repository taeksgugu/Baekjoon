'''
초기 풀이 과정: 처음에 잘못 생각해서 왜 벽돌의 크기가 1인건 깨지지 않는지 한참 고민함
              이후 해당 벽돌의 크기-1만큼 주변 벽돌을 깨뜨리는걸 파악하고 진행하
              크게 두가지 함수 생각 -> 깨뜨릴 구슬을 주면 구현하는 함수 & 백트래킹
              중력 작용 따로 하려고 했는데 그러면 백트래킹 함수가 복잡해질 것 같아서 breakstone에 포함시킴

과정 피드백 : 마지막 테케에서 실수함 이유는 N개가 되기 전에 다 깨뜨려버리는 경우가 발생할 수 있음
            그 경우 answer 값이 갱신이 되지 않음! -> 그래서 answer 값이 초기값 그대로면 0을 반환하게 만듦
            단순히 answer 값 갱신이 안되는거로 만들면 엣지케이스 발생 가능성이 있다고 생각하고 중간 가지치기 추가
'''
from collections import deque
### 처음으로 깨지는 구슬 위치가 주어지면 다 부시고 난 후의 배열을 돌려주는 함수
def breakstone(i,j, arr):
    global H, W
    newarr = [e[:] for e in arr]
    q = deque()
    q.append((i,j, newarr[i][j])) ### q에 삽입할 때, 주변 몇개의 벽돌을 깨야하는지도 같이 삽입
    newarr[i][j] = 0
    while q:
        ci, cj, ck = q.popleft()
        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
            for k in range(1,ck):
                ni, nj = ci+di*k, cj+dj*k
                if 0<=ni<H and 0<=nj<W and newarr[ni][nj] != 0:
                    q.append((ni,nj,newarr[ni][nj]))
                    newarr[ni][nj] = 0

    for i in range(H-1):
        for j in range(W):
            ni, nj = i, j
            while 0<=ni and 0<newarr[ni][nj] and newarr[ni+1][nj] == 0:
                newarr[ni][nj], newarr[ni+1][nj] = newarr[ni+1][nj], newarr[ni][nj]
                ni -= 1
    return newarr

### 깨뜨릴 구슬 정하는 함수 (백트래킹)
def choosball(n, arr):
    global answer
    if n == N: ### 종료조건
        cnt = len([x for y in arr for x in y if x != 0])
        answer = min(answer, cnt)
        return
    
    if len([x for y in arr for x in y if x != 0]) == 0: ### 중간에 다 깨지면 걍 반환
        answer = 0
        return
    
    for j in range(W): ### 가로에서 하나 고르기
        for i in range(H):
            if arr[i][j] != 0:
                choosball(n+1, breakstone(i,j,arr))
                break ### 맨 위 구슬을 깨뜨리면 됨

T = int(input())
for tc in range(1,T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    answer = 1e9
    choosball(0, arr)
    if answer == 1e9: answer = 0 ### 먄약 변동이 없다면
    print(f"#{tc} {answer}")