import sys
input = sys.stdin.readline

arr = [[0]*101 for _ in range(101)]

for _ in range(4):
    a, b, c, d = map(int, input().split())
    for i in range(a, c):
        for j in range(b, d):
            arr[i][j] = 1
print(sum(map(sum,arr)))