INF = 10 ** 9
tc = 1
### 전체 방문 여부 확인 함수
def check():
    return arr == [['*']*M for _ in range(N)]

### 전체 진행 재귀 함수
def solve(si, sj, cnt):
    global answer
    if check(): ### 종료 조건
        answer = min(answer, cnt)
    if cnt>=answer: return ## 가지치기
    for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
        lst = []
        ni, nj = si, sj
        while True:
            ni, nj = ni+di, nj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == '.':
                lst.append((ni,nj))
                arr[ni][nj] = '*' 
            else: break
        if lst: solve(ni-di, nj-dj, cnt+1)
        for ki, kj in lst: 
            arr[ki][kj] = '.'

while True:
    try:
        N, M = map(int, input().split())
        arr = [list(input()) for _ in range(N)]
        answer = 1e9
        for i in range(N):
            for j in range(M):
                if arr[i][j] == '.':
                    arr[i][j] = '*' 
                    solve(i, j, 0)
                    arr[i][j] = '.'
        if answer == 1e9: answer = -1
        print(f"Case {tc}: {answer}")
        tc += 1
    except: break