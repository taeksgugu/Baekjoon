### 경사로 만들 수 있는지 체크하는 함수
def check(lst):
    start, cnt = lst[0], 1
    idx = 1
    while idx<N:
        num = lst[idx]
        if start == num: cnt += 1
        else:
            if start>num:
                if start-num == 1:
                    for k in range(1,L):
                        if idx+k<N and lst[idx+k]==num:
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

T = int(input())
for tc in range(1, T+1):
    N, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr_T = list(map(list, zip(*arr)))
    totalcnt = 0
    for lst in arr:
        if check(lst): totalcnt+=1
    for lst in arr_T:
        if check(lst): totalcnt+= 1
    print(f"#{tc} {totalcnt}")