import sys
input = sys.stdin.readline
N = int(input().rstrip())
minscore, maxscore = 9*N, 0
for idx in range(N):
    lst = list(map(int, input().rstrip().split()))
    if idx == 0:
        q_max, q_min = lst[:], lst[:]
    else:
        q_max = [max(q_max[0], q_max[1]) + lst[0], max(q_max) + lst[1], max(q_max[1], q_max[2]) + lst[2]]
        q_min = [min(q_min[0], q_min[1]) + lst[0], min(q_min) + lst[1], min(q_min[1], q_min[2]) + lst[2]]
print(max(q_max), min(q_min))