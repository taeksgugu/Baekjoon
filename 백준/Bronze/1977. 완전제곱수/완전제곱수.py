import sys, math
input = sys.stdin.readline
M = int(input().rstrip())
N = int(input().rstrip())
lst = []
for num in range(int(math.sqrt(M)), int(math.sqrt(N)+1)):
    if M<=num**2<=N:
        lst.append(num**2)
if lst:
    print(sum(lst))
    print(lst[0])
else:
    print(-1)