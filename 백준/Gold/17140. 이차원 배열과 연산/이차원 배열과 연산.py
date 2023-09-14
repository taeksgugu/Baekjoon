### 초기 풀이과정 -> 3*3 arr를 만들고 행수와 열수를 체크할 변수를 따로 선언한 후에 갱신하면서 R연산 C연산 골라서 진행하는 방식
###               수를 세는 방식을 처음에는 count()함수를 이용할까 하다가 딕셔너리 사용하기로 결정 -> 시간 단축 및 새 리스트 생성이 용이
### 실수 : rownum, colnum 초기 변수 선언할 때, 3,3이 아닌 R,C로 습관처럼 선언해서 10분 이상 소모함...
###       arr 선언도 range(R)로 해서 계속 오답 발생 (어쩐지 Enter 안 눌러도 답이 나옴...)
###       처음에 maxcol,maxrow를 갱신하기 위한 colnum, rownum 변수를 선언하고 리스트 요소를 순회할 때마다 2를 추가했음
###       -> 리스트에 중복 요소가 있을 경우, 2를 추가하면 안되는데 추가해서 패딩할 때 0이 미친듯이 많아짐
###       -> newlst의 길이와 비교해서 갱신하는 방식으로 바꿈
###       최대길이 100을 처음에 고려하지 않음 -> 위의 오류를 고치는 과정에서 스스로 발견하게 되어서 같이 고침
###       마지막 테케에서 깨달은 또 다른 부분은 당연히 R과 C가 배열 범위 안에 있을 줄 알았음...(너무 문제를 믿었음)
###       1시간이 지나고 처음부터 다시 작성할 때 해당 부분들을 고려해서 다시 작성해서 바로 통과함 (진짜 주기적인 reset이 중요하다고 느낌)

### 1차 시도 : 116268kb 196ms 풀이 시간 : 1시간 반

### 아쉬운점 : 풀이과정 및 사용할 자료구조 등은 잘 계획했지만, 디테일 부분에서 상세하게 캐치하지 못해서 디버깅하고 수정하는데 많은 시간을 소모함
###         실제로 테케가 충분하지 않았다면, 이 실수들을 캐치하지 못하고 제출해서 틀렸을 거라고 생각함
### 괜찮은점 : newlst 선언할때 진짜 깔끔하게 숏코딩 잘한 듯(뿌듯)
### 교훈 : 1시간 넘게 오류 찾을 바에 30분 빠르게 새 코드를 작성하자

import sys
input = sys.stdin.readline
### 입력받기
R, C, K = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(3)]

### 문제 풀이 함수
def solve():
    global arr
    rownum, colnum = 3, 3 ### 처음엔 다 3*3 무조건
    for time in range(100):
        if 0<=R-1<rownum and 0<=C-1<colnum and arr[R-1][C-1] == K: ## 첨부터 해당될수도있음
            return time
        if rownum >= colnum: ### 행수가 열수보다 크거나 같으면
            maxcol = 0
            newarr = []
            for idx in range(rownum):
                numdic = {}
                for num in arr[idx]: ### 순회하면서 딕셔너리에 해당 숫자 갯수 갱신
                    if num == 0: continue
                    try: numdic[num] += 1
                    except: numdic[num] = 1
                newlst = [x for y in sorted(numdic.items(), key=lambda x: (x[1],x[0])) for x in y] ### 딕셔너리를 바로 리스트로 변경시키기
                newarr.append(newlst)
                maxcol = max(maxcol, len(newlst)) ### 패딩을 위한 최대 길이 갱신
            ### 패딩 작업 진행
            if maxcol > 100: maxcol = 100 ### 최대 길이 100
            for idx in range(rownum):
                if len(newarr[idx]) > maxcol:
                    newarr[idx] = newarr[idx][:maxcol]
                else:
                    newarr[idx] += [0] * (maxcol-len(newarr[idx]))
            colnum = maxcol ### 열 수 갱신
        else:
            arr_T = list(map(list, zip(*arr)))
            maxrow = 0
            newarr = []
            for jdx in range(colnum):
                numdic = {}
                for num in arr_T[jdx]:
                    if num == 0: continue
                    try: numdic[num] += 1
                    except: numdic[num] = 1
                newlst = [x for y in sorted(numdic.items(), key=lambda x: (x[1], x[0])) for x in y]
                newarr.append(newlst)
                maxrow = max(maxrow, len(newlst))
            ### 패딩 작업 진행
            if maxrow > 100: maxrow = 100 ### 최대 길이 100
            for jdx in range(colnum):
                if len(newarr[jdx]) > maxrow:
                    newarr[jdx] = newarr[jdx][:maxrow]
                else:
                    newarr[jdx] += [0] * (maxrow-len(newarr[jdx]))
            rownum = maxrow ### 행 수 갱신
            newarr = list(map(list, zip(*newarr))) ### 다시 회전시켜줘야함!!!!
        arr = newarr

    if 0 <= R - 1 < rownum and 0 <= C - 1 < colnum and arr[R - 1][C - 1] == K: ### for 문 안에서 캐치를 못하기 때문...
        return 100
    return -1
print(solve())