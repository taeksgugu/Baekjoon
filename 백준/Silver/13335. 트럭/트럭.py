import sys
from collections import deque
input = sys.stdin.readline
### 입력 받기
N, W, L = map(int, input().split())
trucklst = deque(list(map(int,input().split())))
cnt = N
def solve():
    bridge = deque([0]*W)
    answer, remain = 0, N
    total = sum(bridge)
    while remain>0: ### 모든 트럭이 다리를 건널떄까지
        answer += 1
        k = bridge.popleft()
        total -= k
        if k != 0: remain -= 1
        if trucklst:
            if total+trucklst[0] <= L:
                new = trucklst.popleft()
                bridge.append(new)
                total += new
            else: bridge.append(0)
    return answer
print(solve())