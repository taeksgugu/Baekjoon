import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
inningscore = [list(map(int, input().rstrip().split())) for _ in range(N)]
### 타순 만들기
batting_order = []
visited = [0] * 9
cnt = 0
def makecomb(n,lst):
    global cnt
    if n == 8:
        lst.insert(3,0)
        batting_order.append(tuple(lst)) ### 1번 선수는 무조건 4번 타자!
        cnt += 1
        return
    for i in range(1, 9):
        if visited[i] == 0:
            visited[i] = 1
            makecomb(n+1, lst+[i])
            visited[i] = 0
makecomb(0,[])

### 이닝별 득점 비교
answer_score = 0
for battingcomb in batting_order: ## 타순 조합별로 확인
    total_score = 0
    idx = 0  ### 몇 번 타자인지
    for inning in inningscore:
        cnt = 0 ### 아웃 수
        first, second, third = 0, 0, 0 ### 주자들 1루, 2루, 3루
        while cnt<3:
            score = inning[battingcomb[idx]]
            if score == 0:
                cnt += 1
            elif score == 1:
                total_score += third
                first, second, third = 1, first, second
            elif score == 2:
                total_score += (second+third)
                first, second, third = 0, 1, first
            elif score == 3:
                total_score += (first+second+third)
                first, second, third = 0, 0, 1
            else:
                total_score += (first + second + third + 1)
                first, second, third = 0, 0, 0
            idx = (idx+1)%9
    answer_score = max(answer_score, total_score)
print(answer_score)