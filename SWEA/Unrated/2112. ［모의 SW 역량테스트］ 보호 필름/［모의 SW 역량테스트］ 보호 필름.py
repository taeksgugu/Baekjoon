### 주어진 보호필름 강화 테스트 함수
# def check():
#     for lst in list(map(list, zip(*arr))):
#         if not ('0' * K in ''.join(lst) or '1' * K in ''.join(lst)):
#             return False
#     return True
def check():
    for j in range(W):
        same = 1
        for i in range(D-1):
            if same == K: break
            elif arr[i][j] == arr[i+1][j]: same += 1
            else: same = 1
        if same != K: return False
    return True
### 몇 행에 약물 투입할지 백트래킹 함수
def film(n, idx):
    global answer
    if check():
        answer = min(answer, n)
        return
    if n >= answer: return
    for i in range(idx+1, D):
        if v[i] == 0:  ### 아직 약품 투입 안한 열이라면
            v[i] = 1
            lst = arr[i]
            arr[i] = ['0'] * W
            film(n+1, i)
            arr[i] = ['1'] * W
            film(n+1, i)
            v[i] = 0
            arr[i] = lst
T = int(input())
for tc in range(1, T+1):
    D, W, K = map(int, input().split())
    arr = [input().split() for _ in range(D)]
    v = [0] * D
    answer = K
    if K == 1: answer = 0
    else: film(0, -1)
    print(f"#{tc} {answer}")