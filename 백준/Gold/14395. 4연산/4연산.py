import sys, math
from collections import deque
input = sys.stdin.readline
S, T = map(int, input().rstrip().split())

def bfs():
    if S == T: return 0
    elif T == 1: return '/'
    elif T == 0: return '-'
    elif T%S == 0 or int(math.log2(T)) == math.log2(T):
        q = deque()
        v = []
        v.append(S)
        q.append((S, ''))
        t = 0
        while q:
            for _ in range(len(q)):
                num, s = q.popleft()
                if num**2 == T: return s+'*'
                else:
                    if num**2 < T and num**2 not in v:
                        q.append((num**2, s+'*'))
                        v.append(num**2)
                if num*2 == T: return s+'+'
                else:
                    if num*2 < T and num*2 not in v:
                        q.append((num*2, s+'+'))
                        v.append(num * 2)
                if t == 0:
                    q.append((1, '/'))
                    t = 1

    return -1
print(bfs())