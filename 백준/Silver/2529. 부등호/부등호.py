import sys
input = sys.stdin.readline
N = int(input().rstrip())
signlst = input().rstrip().split()
answerlst = []
visited = [0] * 10
def makecomb(n,lst):
    if n == N+1:
        answerlst.append(''.join([str(x) for x in lst]))
        return
    ###
    if n == 0:
        for i in range(10):
            if visited[i] == 0:
                visited[i] = 1
                makecomb(n+1, lst+[i])
                visited[i] = 0
    else:
        if signlst[n-1] == '<':
            for i in range(lst[-1]+1, 10):
                if visited[i] == 0:
                    visited[i] = 1
                    makecomb(n+1, lst+[i])
                    visited[i] = 0
        else:
            for i in range(lst[-1]):
                if visited[i] == 0:
                    visited[i] = 1
                    makecomb(n+1, lst+[i])
                    visited[i] = 0

makecomb(0,[])
answerlst.sort()
print(answerlst[-1])
print(answerlst[0])