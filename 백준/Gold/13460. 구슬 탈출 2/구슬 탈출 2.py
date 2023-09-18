### 초기 풀이 과정: 최대 10회이고 N과 M의 범위가 작기 때문에 BFS로 풀이 가능하다고 판단
### 1차 시도 : 틀렸습니다 풀이 시간: 1시간
###          이유 : 파란 구슬이 중간에 혼자 구멍에 들어가는 경우를 빠뜨린 듯함
### 2차 시도 : 틀렸습니다 수정 시간: 10분
###          위의 파트를 수정하고 전체적으로 다시 다 디버깅해봄
###          또 빠뜨린 파트가 있는 것 같음
### 3,4,5,6,7 차 시도 : 틀렸습니다 & 시간초과
###          새로 코드를 작성해서 시도해봤는데 그 과정에서 오히려 if 문 실수 발생(시간초과)
###          디버깅한다고 적어놓은 print문 그대로 제출
### 8차 시도:
###         좌표 관리 방식을 바꿔보려고 함함
import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j ### 빨간 구슬 좌표
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi, bj = i, j ### 파란 구슬 좌표
            arr[i][j] = '.'
        elif arr[i][j] == 'O': hole_i, hole_j = i, j ### 구멍 좌표
#
# for l in arr:
#     print(*l)

# print(ri,rj,bi,bj, hole_i, hole_j)
### 방향 리스트
dirlst = [(-1,0), (1,0), (0,-1), (0,1)] ### 상 하 좌 우

### 디버깅용
dirq = {-1:'처음', 0:'상', 1:'하', 2:'좌', 3:'우'}
def bfs():
    global ri,rj,bi,bj, hole_i, hole_j
    q = deque()
    q.append((0, -1, ri, rj, bi, bj))  ### 횟수, 이전 기울이기 방향, 빨간 구슬 좌표, 파란 구슬 좌표

    while q:
        n, before, beforeri, beforerj, beforebi, beforebj = q.popleft()
        # ri, rj, bi, bj = beforeri, beforerj, beforebi, beforebj

        if n>=10: continue ### 10회 넘으면 의미 X
        if beforeri == hole_i and beforerj == hole_j and not (beforebi==hole_i and beforebj==hole_j): ### 구멍에 나올 경우, 파란구슬은 동시에 안됨!
            return n

        for i in range(4): ### 4개의 기울일 수 있는 방향
            di, dj = dirlst[i]
            ### 여기서 중요한건 해당 방향으로 기울일 때 우선순위가 있다는 점 (ex 위로 기울일 때 파란 구슬이 빨간 구슬보다 위에 있다면 파란구슬부터 이동)
            prior = 'blue'
            if i == 0: ### 위로 갈 때
                if beforeri<=beforebi:
                    firsti, firstj, secondi, secondj = beforeri, beforerj, beforebi, beforebj
                    prior = 'red'
                else:
                    firsti, firstj, secondi, secondj = beforebi, beforebj, beforeri, beforerj
            elif i == 1: ### 아래로 갈 때
                if beforeri>=beforebi:
                    firsti, firstj, secondi, secondj = beforeri, beforerj, beforebi, beforebj
                    prior = 'red'
                else:
                    firsti, firstj, secondi, secondj = beforebi, beforebj, beforeri, beforerj
            elif i == 2: ### 왼쪽으로 갈 때
                if beforerj<=beforebj:
                    firsti, firstj, secondi, secondj = beforeri, beforerj, beforebi, beforebj
                    prior = 'red'
                else:
                    firsti, firstj, secondi, secondj = beforebi, beforebj, beforeri, beforerj
            else: ### 오른쪽으로 갈 때
                if beforerj>=beforebj:
                    firsti, firstj, secondi, secondj = beforeri, beforerj, beforebi, beforebj
                    prior = 'red'
                else:
                    firsti, firstj, secondi, secondj = beforebi, beforebj, beforeri, beforerj

            first, second = True, True
            while first or second: ### 둘다 False면 멈추기
                fni, fnj, sni, snj = firsti+di, firstj+dj, secondi+di, secondj+dj
                ### 우선 움직이는 것부터 확인
                if first:
                    if arr[fni][fnj] == '.':
                        firsti, firstj = fni, fnj
                    elif arr[fni][fnj] == 'O': ### 이동 가능하다면(구멍 포함)
                        firsti, firstj = fni, fnj
                        # print('구멍',fni,fnj)
                        first = False
                    else: ### 장애물이어서 못간다면 (우선 움직이기 때문에 다른 구슬 확인 필요 x)
                        # print('장애', fni, fnj, arr[fni][fnj])
                        first = False
                if second:
                    if arr[sni][snj] == '.': ### 해당 칸이 빈칸이라면
                        if sni == firsti and snj == firstj: ## 이동하려는 칸에 다른 구슬이 있다면?
                            # print('구슬', sni,snj)
                            second = False
                        else:
                            secondi, secondj = sni, snj
                    elif arr[sni][snj] == 'O': ### 구멍이라면 (앞에서 들어갔던 안 들어갔던 나오기 때문에 갈 수 있음)
                        secondi, secondj = sni, snj
                        # print('구멍', sni, snj)
                        second = False
                    else: ### 장애물이어서 못간다면 (우선 움직이기 때문에 다른 구슬 확인 필요 x)
                        # print('장애', sni,snj)
                        second = False

            if prior == 'red': ### 빨간색이 우선이었다면
                ri, rj, bi, bj = firsti, firstj, secondi, secondj
            else: ### 파란색이 우선이었다면
                ri, rj, bi, bj = secondi, secondj, firsti, firstj
            # print(n, dirq[before], dirq[i], prior, beforeri, beforerj, beforebi, beforebj, ri, rj, bi, bj)
            if ri == hole_i and rj == hole_j and not (bi == hole_i and bj == hole_j):  ### 구멍에 나올 경우, 파란구슬은 동시에 안됨!
                # print('먼저 끝', dirq[i])
                return n+1
            elif bi == hole_i and bj == hole_j: continue ### 동시 구멍 진입 시 or 파란 구슬만 구멍에 들어갈 경우
            elif beforeri==ri and beforerj== rj and beforebi==bi and beforebj==bj: continue ### 제자리인 경우
            else:
                q.append((n+1, i, ri, rj, bi, bj))
        # print()
    return -1
print(bfs())