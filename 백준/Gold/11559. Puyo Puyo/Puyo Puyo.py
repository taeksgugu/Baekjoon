import sys
from collections import deque
input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(12)]

### 없앨 목록 만들기
def makedelete():
    visited = [[0]*6 for _ in range(12)]
    deletelst = []
    for i in range(12):
        for j in range(6):
            if arr[i][j] != '.' and visited[i][j] == 0:
                color = arr[i][j]
                q = deque()
                q.append((i,j))
                visited[i][j] = 1
                cnt = 1
                while q:
                    ci, cj = q.popleft()
                    for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                        ni, nj = ci+di,cj+dj
                        if 0<=ni<12 and 0<=nj<6 and visited[ni][nj] == 0 and arr[ni][nj] == color:
                            cnt += 1
                            q.append((ni,nj))
                            visited[ni][nj] = 1
                if cnt >= 4:
                    deletelst.append((i,j))
    return deletelst
### 없앨 목록에 맞춰서 다 없애고 내려오게 만들기
def update():
    ### 제거
    for i,j in deletelst:
        q = deque()
        q.append((i,j))
        color = arr[i][j]
        arr[i][j] = '.'
        while q:
            ci, cj = q.popleft()
            for di,dj in [(0,1),(0,-1),(1,0),(-1,0)]:
                ni, nj = ci+di, cj+dj
                if 0<=ni<12 and 0<=nj<6 and arr[ni][nj] == color:
                    q.append((ni,nj))
                    arr[ni][nj] = '.'
    ### 내려오기
    arr_T = list(map(list, zip(*arr)))
    newarr_T = []
    for lst in arr_T:
        dotcnt = lst.count('.')
        lst = ['.']*dotcnt + [x for x in lst if x != '.']
        newarr_T.append(lst)
    newarr = list(map(list, zip(*newarr_T)))
    return newarr

answer = 0
while True:
    deletelst = makedelete()
    if deletelst:
        arr = update()
        answer += 1
        # for l in arr:
        #     print(''.join(l))
        # print()
    else:
        print(answer)
        break