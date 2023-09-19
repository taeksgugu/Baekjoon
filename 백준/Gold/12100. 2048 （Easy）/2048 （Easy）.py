### 초기 풀이 : 우선 문제를 읽고 어느 방향으로 정해지든 각 행열 리스트를 합치는 함수를 만들면 된다고 새악ㄱ
###          시간복잡도를 생각해봤는데 최대 5번 이동은 4^5로 2^10, 약 10^3이다.
###          N=20일 경우, 합치는데 걸리는 시간이 최대 400, 4*10^2로 시간 내 가능하다고 판단

### L과 R의 경우 2048을 돌릴 때 그대로 arr에서 가져오기 때문에 기존 arr에 영향을 끼침
# (U,D는 돌리는 과정에서 상관이 없어짐)
import sys
input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

### 몰아서 합쳐주는 2048 게임 함수 생성
def game(lst):
    newlst = []
    before = lst.pop(0)
    for _ in range(len(lst)):
        num = lst.pop(0)
        if num == 0: continue ### 빈칸이어서 무시
        if before == num:
            newlst.append(before+num)
            before = 0
        else: ### 다르다면
            if not before:
                before = num
            else:
                newlst.append(before)
                before = num
    newlst.append(before)
    return newlst+[0]*(N-len(newlst))

def twfe(arr, dir): ### 넣는 배열과 방향
    if dir == 'U': ### 위로 간다면
        newlst = []
        for lst in list(map(list, zip(*arr))):
            newlst.append(game(lst))
        return list(map(list, zip(*newlst)))
    elif dir == 'D': ### 아래로 간다면
        newlst = []
        for lst in list(map(list, zip(*arr))):
            newlst.append((game(lst[::-1]))[::-1])
        return list(map(list, zip(*newlst)))
    elif dir == 'L': ### 왼쪽으로 간다면
        newlst = []
        for lst in [e[:] for e in arr]:
            newlst.append(game(lst))
        return newlst
    elif dir == 'R': ### 오른쪽이라면
        newlst = []
        for lst in [e[:] for e in arr]:
            newlst.append((game(lst[::-1]))[::-1])
        return newlst

### 최대 5번 돌리기 start
answer = 0
def solve(n, gamearr):
    global answer
    # for l in gamearr:
    #     print(*l)
    # print()
    maxval = max(map(max,gamearr))
    answer = max(answer, maxval)

    if n == 5: return
    for dir in ['U','D','L','R']:
        # print(n, dir)
        solve(n+1, twfe(gamearr,dir))

solve(0,arr)
print(answer)