import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
arr = [int(input()) for _ in range(N)]
dp = [0] * (K+1)
dp[0] = 1
for num in arr:
    for i in range(num, K+1):
        dp[i] = dp[i] + dp[i-num]
print(dp[-1])