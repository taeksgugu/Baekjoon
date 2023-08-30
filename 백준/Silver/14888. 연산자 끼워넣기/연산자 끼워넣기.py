import sys
input = sys.stdin.readline
### 값 입력받고 연산자 리스트 생성
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
callst = list(map(int, input().rstrip().split()))
minnum = 1e9
maxnum = -1e9
### 연산자 번호에 따른 함수 딕셔너리 생성
caldict = {0:lambda x,y:x+y,
           1:lambda x,y:x-y,
           2:lambda x,y:x*y,
           3:lambda x,y:x//y if x>=0 else -(-x//y)}
def dfs(n, num):
    global minnum, maxnum
    if n==N:
        minnum = min(num,minnum)
        maxnum = max(num,maxnum)
        return
    for i in range(4):
        if callst[i]:
            callst[i] -= 1
            dfs(n+1, caldict[i](num, arr[n]))
            callst[i] += 1
dfs(1,arr[0])
print(maxnum)
print(minnum)