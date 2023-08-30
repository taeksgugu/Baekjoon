import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = [(0,0)]+[list(map(int, input().rstrip().split())) for _ in range(N)]
answer = 0
def consult(n, money, arr):
    global answer
    if n == N:
        if money > answer:
            answer = money
        return
    for i in range(n+1, N+1):
        if lst[i][0] + i > N+1:
            consult(N, money, arr)
        else:
            consult(i+lst[i][0]-1, money+lst[i][1], arr+[lst[i]])
consult(0,0,[])
print(answer)