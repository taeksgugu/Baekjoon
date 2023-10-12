import sys
input = sys.stdin.readline

N, m, M, T, R = map(int, input().split())
def solve():
    if M < m+T: return -1
    now, time, remain = m, 0, N
    while remain>0:
        if now+T<=M:
            now += T
            remain -= 1
        else:
            now -= R
            now = max(now, m)
        time += 1
    return time

print(solve())