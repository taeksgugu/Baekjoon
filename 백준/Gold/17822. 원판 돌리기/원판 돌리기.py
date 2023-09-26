'''
초기풀이과정: 원판 수를 어떻게 관리할지 고민했다가 배열을 그대로 사용하면 되겟다고 판단
            여기서 주의할 점은 인접 칸 관리인데 행으로는 기존 배열과 다를게 없지만, 열은 연결된다는걸 파악
            원판 수 남아 있을 경우, 확인하는 과정에서 인접하면 같은 수를 다 지우고,
            없으면 평균내서 진행하는 부분을 함수 처리하는게 좋다고 판단
'''
import sys
from collections import deque
input = sys.stdin.readline

N, M, T = map(int, input().split()) ### N개 원판, M개 수
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
orderlst = [list(map(int, input().split())) for _ in range(T)]
def turn(x, d, k): ### 회전시키는 함수
    newarr = []
    for num in range(N):
        if (num+1)%x != 0: ### 원판 번호가 x의 배수가 아니면
            newarr.append(arr[num])
        else:
            lst = arr[num][:]
            if d == 0: lst = lst[-k:] + lst[:-k]### 시계 방향
            else: lst = lst[k:] + lst[:k]
            newarr.append(lst)
    return newarr

def checknum():
    flag = False ### 인접한 수가 있는지
    visited = [[0]*M for _ in range(N)] ### 방문처리
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and visited[i][j] == 0: ### 수가 있다면 확인
                visited[i][j]  = 1
                ### 우선 인접한 칸에 같은 수가 있는지 확인(있으면 순회 시작, 없으면 넘어감)
                if arr[i][(j-1)%M] == arr[i][j] or arr[i][(j+1)%M] == arr[i][j] or (0<=i-1<N and arr[i-1][j] == arr[i][j]) or (0<=i+1<N and arr[i+1][j] == arr[i][j]):
                    flag = True ### 인접한 수가 있다
                    num = arr[i][j]
                    q = deque()
                    q.append((i,j))
                    arr[i][j] = 0 ### 해당 수 삭제
                    while q:
                        ci, cj = q.popleft()
                        for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                            ni, nj = ci+di, (cj+dj)%M
                            if 0<=ni<N and arr[ni][nj] == num and visited[ni][nj] == 0:
                                visited[ni][nj] = 1
                                arr[ni][nj] = 0
                                q.append((ni,nj))

    if flag: ### 인접한 수가 있었다면
        return
    else: ### 없었다면
        total, cnt = 0, 0
        for i in range(N):
            for j in range(M):
                if arr[i][j] > 0:
                    total += arr[i][j]
                    cnt += 1
        if cnt == 0: return
        average = total/cnt
        for i in range(N):
            for j in range(M):
                if arr[i][j]>0: ### 수가 있다면 처리 (큰수, 작은수, 같은 경우도 있을 것 같아서 if elif로 처리)
                    if arr[i][j] > average: arr[i][j] -= 1
                    elif arr[i][j] < average: arr[i][j] += 1
        return

### 디버깅
# print('초기')
# for l in arr:
#     print(*l)
# print()

for x, d, k in orderlst:
    arr = turn(x,d,k)

    # ### 디버깅
    # print('다음단계')
    # print('회전 후')
    # for l in arr:
    #     print(*l)
    # print()

    checknum()
    # ### 디버깅
    # print('체크 후')
    # for l in arr:
    #     print(*l)

print(sum(map(sum, arr)))