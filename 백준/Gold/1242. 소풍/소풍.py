import sys
input = sys.stdin.readline
### 입력 받기
N, K, M = map(int, input().split())

def solve():
    dongho = M-1 # 동호 위치
    start = 0
    remain = N
    for i in range(1, remain+1):
        removed = (start+K-1)%remain
        if removed == dongho: return i ### 동호면
        if removed < dongho: dongho -= 1 ### 동호보다 앞이면
        start = removed
        remain -= 1
print(solve())