import sys
input = sys.stdin.readline
def princess(lst,ycnt,scnt):
    global answer
    if ycnt >= 4: ### 임도연파가 4명이 넘어간 경우, 다솜파는 4명이 될 수 없음
        return
    if scnt + ycnt == 7: ### 둘의 합이 7이면 마무리
        if tuple(sorted(lst)) not in answerlst:
            answerlst.add(tuple(sorted(lst)))
            answer += 1
        return
    for ci, cj in lst:
        for di, dj in [(0,1),(0,-1),(1,0),(-1,0)]:
            ni, nj = ci+di, cj+dj
            if 0<=ni<5 and 0<=nj<5 and visited[ni][nj] == 0:
                visited[ni][nj] = 1
                if arr[ni][nj] == 'S':
                    princess(lst+[(ni,nj)], ycnt, scnt+1)
                else:
                    princess(lst+[(ni,nj)], ycnt+1, scnt)
                visited[ni][nj] = 0
arr = [list(input().rstrip()) for _ in range(5)]
visited = [[0]*5 for _ in range(5)]
answerlst = set()
answer = 0
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            visited[i][j] = 1
            princess([(i,j)],0,1)
print(answer)