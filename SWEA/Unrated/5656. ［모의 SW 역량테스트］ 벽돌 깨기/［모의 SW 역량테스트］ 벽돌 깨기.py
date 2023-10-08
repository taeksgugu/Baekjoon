from collections import deque
def breakstone(num, arr):
    q = deque()
    for i in range(H):
        if arr[i][num] != 0:  ### 위에서 떨어질때 부딪힘
            q.append((i, num, arr[i][num]))
            break
    arr[i][num] = 0
    while q:
        ci, cj, size = q.popleft()
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            for k in range(1, size):
                ni, nj = ci + di * k, cj + dj * k
                if 0 <= ni < H and 0 <= nj < W and arr[ni][nj] != 0:
                    q.append((ni, nj, arr[ni][nj]))
                    arr[ni][nj] = 0
    for i in range(H-1):
        for j in range(W):
            ni, nj = i, j
            while 0<=ni<H and 0<arr[ni][nj] and arr[ni+1][nj]==0:
                arr[ni+1][nj], arr[ni][nj] = arr[ni][nj], arr[ni+1][nj]
                ni -= 1
    return arr

def solve(n, arr):
    global answer
    if n==N:
        cnt = len([x for y in arr for x in y if x != 0])
        answer = min(answer, cnt)
        return

    for i in range(W):
        newarr = [e[:] for e in arr]
        solve(n+1, breakstone(i, newarr))

T = int(input())
for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    answer = 1e9
    solve(0, arr)
    print(f"#{tc} {answer}")