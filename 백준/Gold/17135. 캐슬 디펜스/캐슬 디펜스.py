import sys
input = sys.stdin.readline
N, M, D = map(int, input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]

enemy = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == '1': enemy.append((i,j))
enemy.sort(key=lambda x : x[1])         # 거리가 같으면 가장 왼쪽에 있는 적 (j 작은순 정렬)

goungs = [0, 0, 0]  # 궁수 리스트
def dfs(n, i) :     # dfs에 리스트 담지 않고 넘기기 연습중
    global ans
    if n == 3 :
        ans = max(ans, game(goungs, enemy))
        return
    for j in range(i,M) :
        goungs[n] = j
        dfs(n+1, j+1)
def game(goungs, enemy) :
    kill_cnt = 0
    while enemy:
        kill = set()
        for goung in goungs:       # 각각의 궁수들(N, j)에 대해서  가까운 적 찾기
            x, y, d = -1, -1, D+1
            for r, c in enemy :
                n_d = (N-r) + abs(goung - c)
                if n_d < d: x, y, d = r, c, n_d     # 거리가 작아질 때만 갱신
            kill.add((x, y))
        temp = []
        for r, c in enemy:
            if (r, c) in kill: kill_cnt += 1
            elif r < N-1 :
                temp.append((r+1, c))
        enemy = temp               # 턴마다 적의 위치 디버깅하기 좋음~
    return kill_cnt

ans = 0
dfs(0, 0)
print(ans)