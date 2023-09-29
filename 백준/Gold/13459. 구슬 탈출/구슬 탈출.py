import sys
input = sys.stdin.readline
### 입력 받기
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R':
            ri, rj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'B':
            bi, bj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'O':
            hi, hj = i, j
            arr[i][j] = '.'

dirlst = [(-1,0), (1,0), (0,-1), (0,1)]
opposite = {0:1, 1:0, 2:3, 3:2, -1:-1}
answer = 11

# print('구멍', hi,hj)
def game(n, before, ri, rj, bi, bj):
    global answer
    # print(n, before, ri, rj, bi, bj)
    if ri == hi and rj == hj: ### 빨간 사탕 탈출
        if bi == hi and bj == hj: ### 파란 구슬 같이 탈출한다면 실패
            return
        answer = min(answer, n)
        return

    if answer != -1 and n>=answer: return
    if bi == hi and bj == hj: return
    if n == 10: return
    for num in range(4):
        if num != opposite[before]: ###원상복구하는게 아니면
            di, dj = dirlst[num]
            lst = [(ri,rj), (bi,bj)]
            if num == 0: ### 위로 가는거라면
                lst.sort(key=lambda x: x[0])
            elif num == 1: ### 아래로 가는거라면
                lst.sort(key=lambda x: -x[0])
            elif num == 2: ### 왼쪽으로 가는거라면
                lst.sort(key=lambda x: x[1])
            else: ### 오른쪽으로 가는거라면
                lst.sort(key=lambda x: -x[1])

            fi, fj = lst[0]
            si, sj = lst[1]
            if fi==ri and fj==rj: first = 'red'
            else: first = 'blue'
            # print(num, first, fi, fj, si, sj)
            # 1 blue 8 6 4 6
            ### 이제 해당 방향으로 이동
            while True:
                nfi, nfj = fi+di, fj+dj
                if nfi == hi and nfj == hj: ### 구멍에 들어감
                    fi, fj = hi, hj
                    break
                elif arr[nfi][nfj] != '#':
                    fi, fj = nfi, nfj
                else:
                    break
            while True:
                nsi, nsj = si+di, sj+dj
                # print(nsi, nsj)
                if nsi == hi and nsj == hj: ### 구멍에 들어감
                    si, sj = hi, hj
                    break
                elif arr[nsi][nsj] != '#' and not (nsi==fi and nsj==fj):
                    si, sj = nsi, nsj
                else:
                    break

            if first == 'red':
                if not (fi==ri and fj==rj and si==bi and sj==bj):
                    game(n+1, num, fi, fj, si, sj)
            else:
                if not (si==ri and sj==rj and fi==bi and fj==bj):
                    game(n+1, num, si, sj, fi, fj)

game(0,-1,ri,rj,bi,bj)
if answer == 11: print(0)
else: print(1)

