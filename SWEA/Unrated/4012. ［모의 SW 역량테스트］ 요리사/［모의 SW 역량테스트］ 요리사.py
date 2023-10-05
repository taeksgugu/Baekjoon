T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    def check(lst):
        result = 0
        for i in range(N//2):
            for j in range(i+1, N//2):
                a, b = lst[i], lst[j]
                result += arr[a][b]
                result += arr[b][a]
        return result

    answer = 1e9
    def cook(n, alst, blst):
        global answer
        if len(alst) == N//2 and len(blst) ==N//2:
            acnt = check(alst)
            bcnt = check(blst)
            answer = min(abs(acnt-bcnt), answer)
            return
        if n == N: return
        cook(n+1, alst+[n], blst)
        cook(n+1, alst, blst+[n])

    cook(0,[],[])
    print(f"#{tc} {answer}")