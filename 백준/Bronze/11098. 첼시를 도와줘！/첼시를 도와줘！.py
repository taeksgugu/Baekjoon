import sys, math
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    lst = [input().rstrip().split() for _ in range(N)]
    lst.sort(key=lambda x: -int(x[0]))
    print(lst[0][1])