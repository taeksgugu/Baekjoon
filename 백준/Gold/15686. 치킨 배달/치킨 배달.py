'''
오후 1시 15분 start 30분 1차 제출
이전과 같은 실수를 반복함 맨해튼 거리라고 생각해서 바로 계산하면 되는데 굳이 BFS를 해서 시간초과를 시킴...
35분 2차 제출
'''
import sys
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().split())
arr = [list(map(int ,input().rstrip().split())) for _ in range(N)]
houselst, chickenlst = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1: houselst.append((i,j)) ### 집
        elif arr[i][j] == 2: chickenlst.append((i,j)) ### 치킨 집

def calcitydist(lst): ### 도시거리 구하는 함수
    citydist = 0
    for i, j in houselst:
        citydist += min([abs(li-i)+abs(lj-j) for li, lj in lst])
    return citydist

answer = 1e9
def choosechiken(n, idx, lst):
    global answer
    if n == M:
        answer = min(answer, calcitydist(lst))
        return
    for i in range(idx+1, len(chickenlst)):
        choosechiken(n+1, i, lst+[chickenlst[i]])

choosechiken(0,-1,[])
print(answer)