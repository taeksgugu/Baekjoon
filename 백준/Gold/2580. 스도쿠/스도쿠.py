import sys
input = sys.stdin.readline

### 입력 받기
sudoku = [list(map(int, input().split())) for _ in range(9)]
zerolst = [] ### 숫자 넣어야할 좌표리스트

### 행, 열, 3*3칸 숫자 관리
row = [[0]*10 for _ in range(9)] ### row[i][num]은 i번째 행 num은 이미 있음
col = [[0]*10 for _ in range(9)] ### col[j][num]은 j번째 열 num은 이미 있음
square = {(i,j): [0]*10 for i in range(3) for j in range(3)} ### squar[i//3][j//3]을 통해 해당 스퀘어 num 방문 조회

for i in range(9):
    for j in range(9):
        snum = sudoku[i][j]
        row[i][snum] = 1
        col[j][snum] = 1
        square[(i//3,j//3)][snum] = 1
        if snum == 0:
            zerolst.append((i,j))

### 스도쿠 자체 만들기 함수
flag = False
def makesudoku(idx):
    global flag
    if idx == len(zerolst):
        flag = True
        for l in sudoku:
            print(*l)
        return
    if flag: return
    i, j = zerolst[idx]
    # print(i,j, idx)
    for newnum in range(1,10):
        if row[i][newnum] == 0 and col[j][newnum] == 0 and square[(i//3,j//3)][newnum] == 0:
            row[i][newnum] = 1
            col[j][newnum] = 1
            square[(i//3,j//3)][newnum] = 1
            sudoku[i][j] = newnum
            makesudoku(idx+1)
            row[i][newnum] = 0
            col[j][newnum] = 0
            square[(i//3,j//3)][newnum] = 0
            sudoku[i][j] = 0
makesudoku(0)