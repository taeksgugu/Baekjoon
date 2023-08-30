import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
if N == 1:
    arr.append(0)
arr.sort(reverse=True)
answer = 0
while answer<1440 and sum(arr)!= 0:
    if arr[1] != 0:
        arr[0] -= 1
        arr[1] -= 1
    else:
        arr[0] -= 1
    answer += 1
    arr.sort(reverse=True)
if sum(arr) == 0:
    print(answer)
else:
    print(-1)