import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = [[0]*(M+2)] + [[0] + list(map(int, input().rstrip().split())) + [0] for _ in range(N)] + [[0]*(M+2)]
dp = [[0]*(M+2) for _ in range(N+2)]
for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i-1][j-1], dp[i][j-1], dp[i-1][j]) + arr[i][j]
print(dp[N][M])