import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = [0] + [int(input().rstrip()) for _ in range(N)]
dp = [0]*(N+1)
if N == 1:
    print(arr[1])
elif N == 2:
    print(sum(arr))
else:
    dp[1] = arr[1]
    dp[2] = arr[1]+arr[2]
    for i in range(3, N+1):
        dp[i] = max(dp[i-2] + arr[i], dp[i-3]+arr[i-1]+arr[i])
    print(dp[-1])
