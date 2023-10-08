### 입력 받기
def check(arr):
    for j in range(W):
        start, cnt = arr[0][j], 1
        for i in range(1, D):
            num = arr[i][j]
            if start == num: cnt += 1
            else:
                start, cnt = num, 1
            if cnt==K: break
        if cnt<K : return False
    return True

def choosedrug(n, idx, arr):
    global answer
    if check(arr):
        answer = min(answer, n)
        return
    if n>=answer: return
    if n==D: return
    for i in range(idx+1, D):
        newarr = [e[:] for e in arr]
        lst = newarr[i]
        newarr[i] = [0]*W
        choosedrug(n+1, i, newarr)
        newarr[i] = [1]*W
        choosedrug(n+1, i, newarr)
        newarr[i] = lst

T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(D)]
    answer = 1e9
    choosedrug(0,-1,arr)
    print(f"#{tc} {answer}")