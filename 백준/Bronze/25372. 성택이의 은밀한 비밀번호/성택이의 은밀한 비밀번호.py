import sys
input = sys.stdin.readline

### 입력 받기
N = int(input())
for _ in range(N):
    pw = input()
    if 6<=len(pw)-1<=9: print('yes')
    else: print('no')
