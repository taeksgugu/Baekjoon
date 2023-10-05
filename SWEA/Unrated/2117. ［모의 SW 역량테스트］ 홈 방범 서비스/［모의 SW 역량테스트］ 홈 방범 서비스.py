T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    houselst = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1: houselst.append((i,j))

    answer = 0
    for i in range(N):
        for j in range(N):
            maxk = max(N-i, i+1)+max(N-j, j+1)
            for k in range(maxk, 0, -1):
                fee = k*k+(k-1)*(k-1)
                cnt = 0
                for hi, hj in houselst:
                    dist = abs(hi-i)+abs(hj-j)
                    if dist<=k-1: cnt += 1
                if cnt*M>=fee:
                    answer = max(answer, cnt)
                    break

    print(f"#{tc} {answer}")