### 한번 틀린 이유: di,dj 쓸 때 좌표 실수
import sys
from collections import deque
input = sys.stdin.readline
### 기존 입력값 받기
N, M, D = map(int, input().rstrip().split())
arr = []
enemylst = [] ### 적이 있는 리스트 생성
for i in range(N):
    line = input().rstrip().split()
    for j in range(M):
        if line[j] == '1':
            enemylst.append((i,j))
    arr.append(line)

### 궁수 조합에서 제거 가능한 적 수 계산하기
answer = 0
def killenemy(lst):
    killcnt, enemies = 0, enemylst ### 초기화
    while enemies: ### 적이 없어질 때까지
        removelst = set()
        for archer_j in lst: ### 생성된 조합에서 궁수 한명을 뽑아서 한턴 진행
            visited = [[0]*M for _ in range(N)]
            findenemy = deque()
            dist, go = 1, True
            while dist<=D:
                if dist == 1:
                    if (N-1, archer_j) in enemies:
                        removelst.add((N-1, archer_j))
                        break
                    else:
                        findenemy.append((N-1, archer_j))
                        visited[N-1][archer_j] = 1
                        dist += 1
                else:
                    for _ in range(len(findenemy)):
                        i, j = findenemy.popleft()
                        for di, dj in [(0,-1), (-1,0), (0,1)]:
                            ni, nj = i+di, j+dj
                            if (ni,nj) in enemies:
                                removelst.add((ni,nj))
                                go = False
                                break
                            elif 0<=ni<N and 0<=nj<M and visited[ni][nj] == 0:
                                visited[ni][nj] = 1
                                findenemy.append((ni,nj))
                        if not go: break
                    if not go: break
                    dist += 1
        newenemy = []
        for enem_i, enem_j in enemies:
            if (enem_i, enem_j) in removelst: killcnt += 1
            elif enem_i+1 < N: newenemy.append((enem_i+1, enem_j))
        enemies = newenemy
    return killcnt
### 궁수 조합 만들기
answer = 0
def archercomb(n, idx, lst):
    global answer
    if n == 3:
        answer = max(answer, killenemy(lst))
        return
    for i in range(idx+1, M):
        archercomb(n+1, i, lst+[i])
archercomb(0,-1,[])
print(answer)