while True:
    N = int(input())
    if N == 0: break
    lst = [input() for _ in range(N)]
    lst.sort(key=lambda x: x.lower())
    print(lst[0])