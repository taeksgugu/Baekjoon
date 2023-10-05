import sys
input = sys.stdin.readline

### 경사로 만들 수 있는지 체크하는 함수
def check(lst):
    start, cnt = lst[0], 1
    idx = 1
    while idx<N:
        num = lst[idx]
        # print(num)
        if start == num: cnt += 1
        else:
            if start>num:
                if start-num == 1:
                    for k in range(1,L):
                        if idx+k<N and lst[idx+k]==num:
                            # print(num, lst[idx+k])
                            continue
                        else: return False
                    idx += (L-1)
                    start, cnt = num, 0
                else: return False
            else:
                if num-start == 1:
                    if cnt>=L: start, cnt = num, 1
                    else: return False
                else: return False
        idx += 1
    return True
# N, L = 6, 2
# print(check([3, 2, 2, 2, 3, 3]))
### 입력 받기 및 초기 변수 선언
N, L = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_T = list(map(list, zip(*arr)))
totalcnt = 0
for lst in arr:
    if check(lst): totalcnt+=1
    # print(lst)
    # print(check(lst))

# print('세로')
for lst in arr_T:
    if check(lst): totalcnt+= 1
    # print(lst)
    # print(check(lst))

print(totalcnt)