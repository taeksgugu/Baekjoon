import sys
input = sys.stdin.readline
print(sum([x if x >=40 else 40 for x in [int(input().rstrip()) for _ in range(5)]])//5)