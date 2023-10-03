import sys
input = sys.stdin.readline
### 입력 받기
N, K = map(int, input().split())
weightlst = list(map(int, input().split()))

answer = 0
v = [0]*N
def training(n, threesum):
    global answer
    if n == N:
        answer += 1
        return

    for i in range(N):
        if v[i] == 0 and threesum-K+weightlst[i]>=500:
            v[i] = 1
            training(n+1, threesum-K+weightlst[i])
            v[i] = 0

training(0, 500)
print(answer)