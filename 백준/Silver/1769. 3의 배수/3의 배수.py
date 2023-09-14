import sys
input = sys.stdin.readline
num = input().rstrip()
cnt = 0
while len(num) > 1:
    cnt += 1
    num = str(sum(map(int, list(num))))
print(cnt)
if int(num)%3 == 0: print('YES')
else: print('NO')