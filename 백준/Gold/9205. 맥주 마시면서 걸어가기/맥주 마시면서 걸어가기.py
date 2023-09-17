### 13일전에 틀렸던 문제 그 때 풀이과정은 생각이 나지 않음
### 초기 풀이 과정: 입력으로 제공된 좌표만 이용해서 문제를 해결할 예정
###               출발은 상근이네 집에서 하고 페스티벌 장소까지의 거리를 구함
###               맥주 20병으로 못 갈 것 같으면 편의점을 들릴 수 있는지를 확인하면서 DFS 진행 예정

import sys
from collections import deque
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    ### 테스트케이스별 입력 받기
    N = int(input())
    si, sj = map(int, input().split()) ### 상근이집
    martlst = [list(map(int, input().split())) for _ in range(N)]
    ei, ej = map(int, input().split()) ### 페스티벌 위치
    visited = [0]*N ### 편의점 방문 여부 확인
    q = deque()
    q.append((si,sj))

    while q:
        i, j = q.pop()
        if abs(ei-i)+abs(ej-j) <= 1000:
            print('happy')
            break
        for num in range(N):
            mi, mj = martlst[num]
            if visited[num] == 0 and abs(mi - i) + abs(mj - j) <= 1000:
                visited[num] = 1
                q.append((mi,mj))
    else:
        print('sad')