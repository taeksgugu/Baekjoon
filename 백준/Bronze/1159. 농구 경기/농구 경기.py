import sys
input = sys.stdin.readline
N = int(input())
cntdict = {}
for _ in range(N):
    w = input().rstrip()[0]
    if cntdict.get(w): cntdict[w] += 1
    else: cntdict[w] = 1
lst = sorted([x for x in cntdict if cntdict[x]>=5])
if lst: print(''.join(lst))
else: print("PREDAJA")