import sys
from collections import deque
input = sys.stdin.readline
N = int(input().rstrip())
allstate = [i for i in range(1,N+1)]
people = [0] + list(map(int, input().rstrip().split()))
graph = [[] for _ in range(N+1)]
for i in range(1,N+1):
    state = list(map(int, input().rstrip().split()))
    graph[i] = state[1:]
### 선거구 구역 다 연결되었는지 확인
def check(lst):
    newlst = lst[:]
    visited = [0]*(N+1)
    q = deque()
    q.append(lst[0])
    visited[lst[0]] = 1
    while q:
        node = q.pop()
        newlst.remove(node)
        for i in graph[node]:
            if i in newlst and visited[i] == 0:
                visited[i] = 1
                q.append(i)
    if newlst:
        return False
    return True
###
statelst = []
v = [0]*(N+1)
def makestate(n, idx, lst):
    # print(lst)
    if lst and check(lst):
        otherstate = [x for x in allstate if x not in lst]
        if otherstate and check(otherstate):
            statelst.append((lst, otherstate))
    if n==N//2:
        return
    for i in range(idx+1, N+1):
        if v[i] == 0:
            v[i] = 1
            makestate(n+1, i, lst+[i])
            v[i] = 0
makestate(0, 0,[])

if statelst:
    answer = sum(people)
    for case in statelst:
        # print(case)
        people1 = sum([people[x] for x in case[0]])
        people2 = sum([people[x] for x in case[1]])
        answer = min(answer, abs(people1-people2))
    print(answer)
else:
    print(-1)