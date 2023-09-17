import sys
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().split())
lst = sorted(list(map(int, input().split())))
numlst = []

def makecomb(n, idx, number):
    if n == M:
        if number not in numlst:
            print(number[1:])
            numlst.append(number)
        return

    for i in range(idx+1, N):
        makecomb(n+1, i, number + ' ' + str(lst[i]))

makecomb(0,-1,'')