import sys
input = sys.stdin.readline

N = int(input())
lst = []
for _ in range(N):
    name, order = input().split()
    if order == 'enter':
        lst.append(name)
    else:
        lst.remove(name)
lst.sort(reverse=True)
for nn in lst:
    print(nn)