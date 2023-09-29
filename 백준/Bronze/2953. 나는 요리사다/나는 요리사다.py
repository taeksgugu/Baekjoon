arr = [list(map(int, input().split())) for _ in range(5)]
lst = sorted([(num+1, sum(arr[num])) for num in range(5)], key = lambda x: (-x[1]))
print(*lst[0])