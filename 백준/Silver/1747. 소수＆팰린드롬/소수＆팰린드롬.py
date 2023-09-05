import sys
input = sys.stdin.readline
N = int(input().rstrip())
visited = [0]*2000002
i = 2
while i<N:
    if visited[i] == 0:
        for idx in range(i,2000002,i):
            if idx != i:
                visited[idx] = 1
    i += 1
visited[1] = 1
while True:
    if visited[N] == 0 and str(N) == str(N)[::-1]:
        print(N)
        break
    N += 1