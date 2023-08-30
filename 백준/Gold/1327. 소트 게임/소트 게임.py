import sys
input = sys.stdin.readline
from collections import deque
N, K = map(int, input().rstrip().split())
### 모든 조합의 경우 만들기
comb_lst = {}
visited = [0] * N
length = 0
def makecomb(n, lst):
    global length
    if n == N:
        comb_lst[lst] = 0
        length += 1
        return
    for i in range(1, N+1):
        if visited[i-1] == 0:
            visited[i-1] = 1
            makecomb(n+1, lst+str(i))
            visited[i-1] = 0
makecomb(0,'')
def bfs():
    global ans
    q = deque()
    q.append((arr))
    comb_lst[arr] = 1
    cnt = 0
    while q:
        for _ in range(len(q)):
            lst = q.popleft()
            # print(lst, comb_lst)
            if lst == answer:
                return cnt
            for i in range(N-K+1):
                newlst = lst[:i] + lst[i:i+K][::-1] + lst[i+K:]
                if comb_lst[newlst] == 0:
                    comb_lst[newlst] = 1
                    q.append(newlst)
        cnt += 1
    return -1
arr = input().rstrip().split()
arr, answer = ''.join(arr), ''.join(sorted(arr))
print(bfs())