import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = [0] + list(map(int, input().rstrip().split()))
dp = [0] * (N+1)
idx = 1
while idx < N+1:
    dp[idx] = 1
    j = idx-1
    while j>0:
        if arr[j] < arr[idx]:
            dp[idx] = max(dp[idx], dp[j]+1)
        j -= 1
    idx += 1
print(max(dp))