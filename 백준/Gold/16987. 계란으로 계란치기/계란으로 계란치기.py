import sys
input = sys.stdin.readline
N = int(input().rstrip())
slst = []
wlst = []
for _ in range(N):
    s, w = map(int, input().rstrip().split())
    slst.append(s)
    wlst.append(w)
answer = 0
def egg(n):
    global answer

    cnt = len([x for x in slst if x <= 0])
    answer = max(answer, cnt)
    # print(n, cnt, slst)
    if n == N:
        answer = max(answer, cnt)
        return
    if N - cnt == 0:
        answer = N
        return

    if slst[n] <= 0: egg(n+1)
    else:
        for i in range(N):
            if i != n and slst[i] > 0:
                slst[i] -= wlst[n]
                slst[n] -= wlst[i]
                egg(n+1)
                slst[i] += wlst[n]
                slst[n] += wlst[i]

egg(0)
print(answer)