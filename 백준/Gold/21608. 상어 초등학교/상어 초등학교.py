import sys
input = sys.stdin.readline
N = int(input().rstrip())
favor = {}  ## 좋아하는 학생 리스트를 딕셔너리로 받기 위함
for _ in range(N*N):
    lst = list(map(int, input().rstrip().split()))
    favor[lst[0]] = lst[1:]
visited = [[0]*N for _ in range(N)]
for student, favorites in favor.items(): ### 좋아하는 학생 리스트 탐방
    seatlst = []
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0: ### 아직 자리 지정이 되지 않았으면
                lovers = 0
                empty = 0
                for di, dj in [(0,1),(0,-1), (1,0),(-1,0)]: ### 인접 자리 탐방
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N:
                        ### 비어있으면 empty -1 이유는 heapq에서는 작을수록 우선순위를 가짐
                        if visited[ni][nj] == 0:
                            empty -= 1
                        elif visited[ni][nj] in favorites: ### 같은 원리로 좋아하는 학생수 빼기
                            lovers -= 1
                seatlst.append((lovers,empty,i,j))### 우선순위 자리 뽑기
    l, e, a, b = sorted(seatlst)[0]
    visited[a][b] = student

answer = 0
satisfylst = [0,1,10,100,1000]
for i in range(N):
    for j in range(N):
        cnt = 0
        for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  ### 인접 자리 탐방
            ni, nj = i + di, j + dj
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] in favor[visited[i][j]]:
                cnt += 1
        answer += satisfylst[cnt]
print(answer)