### 입력 받기
def cal(lst):
    score = 0
    for i in range(N//2):
        for j in range(i+1, N//2):
            a, b = lst[i], lst[j]
            score += arr[a][b]
            score += arr[b][a]
    return score

def cook(n, a, b):
    global answer
    if len(a)==len(b)==N//2:
        scenergy_a = cal(a)
        scenergy_b = cal(b)
        differ = abs(scenergy_a - scenergy_b)
        answer = min(differ, answer)
        return
    if n==N: return
    cook(n+1, a+[n], b)
    cook(n+1, a, b+[n])
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    answer = 1e9
    cook(0,[],[])
    print(f"#{tc} {answer}")
