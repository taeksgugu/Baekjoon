### 초기 풀이 과정: 보자마자 리스트로 관리해야지라는 마음을 먹었는데 출력을 다 해야하는걸 보고
###               그냥 배열 관리가 더 편할수도 있겠다는 생각을 함
import sys
input = sys.stdin.readline
### 방향리스트 생성
dirlst = {'U':(-1,0), 'D':(1,0), 'L':(0,-1), 'R':(0,1)}
game = 1
### 시작
while True:
    R, C = map(int, input().split())
    if R == 0 and C == 0: break ### 0 0 입력시 정지
    arr = [list(input()) for _ in range(R)]
    destination = []
    success_cnt = 0
    for i in range(R):
        for j in range(C):
            if arr[i][j] == '+': destination.append((i,j))
            elif arr[i][j] == 'B':
                success_cnt += 1 ### 이미 목표점 위에 박스가 있음
                destination.append((i, j))
            elif arr[i][j] == 'w': si, sj = i,j
            elif arr[i][j] == 'W': ### 목표점 위에 캐릭터가 있는 경우
                si, sj = i, j
                destination.append((i, j))
    dest_cnt = len(destination) ### 목표점 도달 박스 수, 목표점 수
    orderlst = list(input().rstrip())
    success_fail = 'incomplete'

    ### 명령 수행 시작
    for order in orderlst:
        di, dj = dirlst[order]
        ni, nj = si+di, sj+dj ### 바깥 둘레가 무조건 벽이어서 범위 확인 필요X
        if arr[ni][nj] == '.': ### 빈공간이라면
            if (si,sj) in destination: ### 캐릭터 기존 위치가 목표점이었다면 'W'에서 'w'로 변경
                arr[si][sj], arr[ni][nj] = '+','w'
            else:
                arr[si][sj], arr[ni][nj] = '.', 'w' ### 해당 위치로 이동
            si, sj = ni, nj

        elif arr[ni][nj] == '+': ### 가려는 곳이 목표점인 경우
            if (si, sj) in destination:  ### 캐릭터 기존 위치가 목표점이었다면
                arr[si][sj], arr[ni][nj] = '+', 'W'
            else:
                arr[si][sj], arr[ni][nj] = '.', 'W'  ### 해당 위치로 이동
            si, sj = ni, nj

        elif arr[ni][nj] == '#': continue ### 벽인 경우

        elif arr[ni][nj] == 'b': ### 빈 칸 위의 박스가 있는 경우
            if arr[ni+di][nj+dj] == '#': continue ### 박스 다음칸이 벽인 경우
            elif arr[ni+di][nj+dj] == 'b' or arr[ni+di][nj+dj] == 'B': continue ### 박스 다음칸이 박스인 경우
            elif arr[ni+di][nj+dj] == '.': ### 박스 다음칸이 빈칸인 경우
                if (si, sj) in destination:  ### 캐릭터 기존 위치가 목표점이었다면
                    arr[si][sj], arr[ni][nj], arr[ni+di][nj+dj] = '+', 'w', 'b'
                    si, sj = ni, nj
                else:
                    arr[si][sj], arr[ni][nj], arr[ni+di][nj+dj] = '.', 'w', 'b' ### 해당 위치로 이동
                    si, sj = ni, nj
            elif arr[ni+di][nj+dj] == '+': ### 박스 다음칸이 목표점인 경우
                if (si, sj) in destination:  ### 캐릭터 기존 위치가 목표점이었다면
                    arr[si][sj], arr[ni][nj], arr[ni+di][nj+dj] = '+', 'w', 'B'
                    success_cnt += 1
                    si, sj = ni, nj
                else:
                    arr[si][sj], arr[ni][nj], arr[ni+di][nj+dj] = '.', 'w', 'B' ### 해당 위치로 이동
                    success_cnt += 1
                    si, sj = ni, nj
        elif arr[ni][nj] == 'B': ### 목표점 위의 박스가 있는 경우
            if arr[ni+di][nj+dj] == '#': continue ### 박스 다음칸이 벽인 경우
            elif arr[ni+di][nj+dj] == 'b' or arr[ni+di][nj+dj] == 'B': continue ### 박스 다음칸이 박스인 경우
            elif arr[ni+di][nj+dj] == '.': ### 박스 다음칸이 빈칸인 경우
                if (si, sj) in destination:  ### 캐릭터 기존 위치가 목표점이었다면
                    arr[si][sj], arr[ni][nj], arr[ni+di][nj+dj] = '+', 'W', 'b'
                    success_cnt -= 1
                    si, sj = ni, nj
                else:
                    arr[si][sj], arr[ni][nj], arr[ni+di][nj+dj] = '.', 'W', 'b' ### 해당 위치로 이동
                    success_cnt -= 1
                    si, sj = ni, nj
            elif arr[ni + di][nj + dj] == '+':  ### 박스 다음칸이 목표점인 경우
                if (si, sj) in destination:  ### 캐릭터 기존 위치가 목표점이었다면
                    arr[si][sj], arr[ni][nj], arr[ni + di][nj + dj] = '+', 'W', 'B'
                    si, sj = ni, nj
                else:
                    arr[si][sj], arr[ni][nj], arr[ni + di][nj + dj] = '.', 'W', 'B'  ### 해당 위치로 이동
                    si, sj = ni, nj
        if success_cnt == dest_cnt:
            success_fail = 'complete'
            break
        # print(order, success_cnt)
        # for l in arr:
        #     print(*l)
        # print()

    print(f'Game {game}: {success_fail}')
    for l in arr:
        print(''.join(l[:-1]))
    game += 1