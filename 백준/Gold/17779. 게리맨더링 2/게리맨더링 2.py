import sys
input = sys.stdin.readline
### 입력 받기
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
def cal(x,y,d1,d2):
    newarr = [[0]*N for _ in range(N)]
    one, two, three, four = 0, 0, 0, 0
    for d in range(d1+1):
        newarr[x+d][y-d] = 5
        newarr[x+d2+d][y+d2-d] = 5
    for d in range(d2+1):
        newarr[x+d][y+d] = 5
        newarr[x+d1+d][y-d1+d] = 5
    for i in range(N):
        idxlst = []
        for idx in range(N):
            if newarr[i][idx] == 5: idxlst.append(idx)
        if idxlst: start, finish = idxlst[0], idxlst[-1]
        else: start, finish = N, N
        for j in range(N):
            if newarr[i][j] == 0:
                if start<=j<=finish:
                    newarr[i][j] = 5
                elif 0<=i<x+d1 and 0<=j<=y:
                    newarr[i][j] = 1
                    one += 1
                elif 0<=i<=x+d2 and y<j<N:
                    newarr[i][j] = 2
                    two += 1
                elif x+d1<=i<N and 0<=j<y-d1+d2:
                    newarr[i][j] = 3
                    three += 1
                elif x+d2<i<N and y-d1+d2<=j<N:
                    newarr[i][j] = 4
                    four += 1

    if one>0 and two>0 and three>0 and four>0: ### 모든 선거구가 최소 구역 ㅎ1개 이상일 때
        sumlst = [0, 0, 0, 0, 0]
        for i in range(N):
            for j in range(N):
                if newarr[i][j] == 1: sumlst[0] += arr[i][j]
                elif newarr[i][j] == 2: sumlst[1] += arr[i][j]
                elif newarr[i][j] == 3: sumlst[2] += arr[i][j]
                elif newarr[i][j] == 4: sumlst[3] += arr[i][j]
                else: sumlst[4] += arr[i][j]

        return max(sumlst) - min(sumlst)
    return 100*N*N

minanswer = 100*N*N
for d1 in range(1, N):
    for d2 in range(1, N):
        if d1+d2 <= N:
            for x in range(N):
                for y in range(N):
                    if 0<=x<x+d1+d2<N and 0<y-d1<y<y+d2<N:
                        val = cal(x, y, d1, d2)
                        minanswer = min(val, minanswer)
print(minanswer)