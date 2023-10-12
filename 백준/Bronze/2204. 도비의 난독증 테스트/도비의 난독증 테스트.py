import sys
input = sys.stdin.readline
while True:
    N = int(input())
    if N == 0: break
    lst = [input().rstrip() for _ in range(N)]
    lst.sort(key=lambda x: x.lower())
    print(lst[0])