import sys
input = sys.stdin.readline

### 입력 받기
idxdict = {0:5, 1:3, 2:4, 3:1, 4:2, 5:0}
def find(num, lst):
    idx = lst.index(num)
    topidx = idxdict[idx]
    topnum = lst[topidx]
    maxnum = max([lst[n] for n in range(6) if n != idx and n != topidx])
    return num, topnum, maxnum


def builddice(num):
    bottom = num
    answer = 0
    for i in range(N):
        bottom, top, maxnum = find(bottom, arr[i])
        answer += maxnum
        bottom = top
    return answer

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
result = 0
for num in range(1, 7):
    ans = builddice(num)
    result = max(result, ans)
print(result)