def find(n):
    if n != p[n]:
        p[n] = find(p[n])
    return p[n]
def union(a,b):
    p[find(b)] = find(a)

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    lst = list(map(int, input().split()))
    p = [n for n in range(N+1)]
    for i in range(M):
        a, b = lst[i*2], lst[i*2+1]
        union(a,b)
    answer = 0
    for num in range(1, N+1):
        if num == p[num]:
            answer += 1

    print(f"#{tc} {answer}")