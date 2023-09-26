import sys
input = sys.stdin.readline

### 입력 받기
while True:
    try:
        N, M = map(int, input().split())
        cnt = 0
        for num in range(N, M+1):
            if len(str(num)) == len(set(list(str(num)))):
                cnt += 1
        print(cnt)
    except:
        break