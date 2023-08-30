N, num = map(int, input().split())
cnt = 0
while num>N:
    cnt += 1
    if num % 10 == 1:
        num //= 10
    elif num % 2 == 0:
            num //= 2
    else:
        break
if num == N:
    print(cnt+1)
else:
    print(-1)