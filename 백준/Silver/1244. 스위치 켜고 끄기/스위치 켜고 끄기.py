import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
for _ in range(M):
    gender, num = map(int, input().rstrip().split())
    if gender == 1:
        for i in range(num-1, N, num):
            arr[i] = 1 - arr[i]
    else:
        i = 0
        while i <= min(num-1, N-num):
            a, b = arr[num-i-1], arr[num+i-1]
            if a == b:
                if i == 0:
                    arr[num-1] = 1 - a
                else:
                    arr[num-i-1] = 1 - a
                    arr[num+i-1] = 1 - b
            else:
                break
            i += 1
for idx in range(0, N, 20):
    print(*arr[idx:idx+20])