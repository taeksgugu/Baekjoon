import sys
input = sys.stdin.readline
N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = N//2*100
def checkpower(lst, n):
    linklst = [p for p in range(N)]
    power_s = 0
    power_l = 0
    for a in range(n-1):
        for b in range(a+1, n):
            power_s += arr[lst[a]][lst[b]]
            power_s += arr[lst[b]][lst[a]]
    for num in lst:
        linklst.remove(num)
    for a in range(n-1):
        for b in range(a+1, n):
            power_l += arr[linklst[a]][linklst[b]]
            power_l += arr[linklst[b]][linklst[a]]
    return abs(power_s-power_l)
def startlink(n, i,lst):
    global answer
    if answer == 0:
        return
    if n == N//2:
        power = checkpower(lst, n)
        answer = min(answer, power)
        # print(lst,power, answer)
        return
    for j in range(i+1, N):
        startlink(n+1, j, lst+[j])
startlink(0,-1,[])
print(answer)