T = int(input())
for tc in range(1, T+1):
    N, K = map(int, input().split())
    lst = list(input())
    numberlst = set()
    for _ in range(N//4):
        for idx in range(4):
            word = lst[(N//4)*idx:(N//4)*(idx+1)]
            numberlst.add(int(''.join(word), 16))
        lst = [lst[-1]] + lst[:-1]

    numberlst = sorted(list(numberlst), reverse=True)
    print(f"#{tc} {numberlst[K-1]}")