import sys
input = sys.stdin.readline

### 입력 받기
N = int(input())
graph = {n:[] for n in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

numlst = list(map(int, input().split()))

def judge(lst):
    nodenum = lst[0]
    if nodenum != 1: return 0
    nextnodelst = []
    for num in lst[1:]:
        # print(nodenum, num, graph[nodenum])
        if num in graph[nodenum]:
            graph[nodenum].remove(num)
            graph[num].remove(nodenum)
            nextnodelst.append(num)
        else:
            return 0

        if not graph[nodenum]:  ### 노드 그래프 다 비워졌으면
            while nextnodelst:
                nextnode = nextnodelst.pop(0)
                if graph[nextnode]:
                    nodenum = nextnode
                    break
                else: continue
    return 1

print(judge(numlst))