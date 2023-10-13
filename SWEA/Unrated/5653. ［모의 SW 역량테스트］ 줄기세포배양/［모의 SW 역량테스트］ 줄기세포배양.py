dirlst = [(-1,0), (1,0), (0,-1), (0,1)]

T = int(input())
for tc in range(1, 1+T):
    N, M, K = map(int, input().split())
    rowlen, collen = N+2*K+2, M+2*K-2
    arr = [[0]*collen for _ in range(rowlen)]
    livedead = [[0]*collen for _ in range(rowlen)]
    for i in range(N):
        data = list(map(int, input().split()))
        for j in range(M):
            arr[i][j] = data[j]
            if data[j] > 0: livedead[i][j] = -(data[j])

    for _ in range(K):
        l = [[0]*collen for _ in range(rowlen)]
        for i in range(rowlen):
            for j in range(collen):
                if arr[i][j] == 0 or arr[i][j] == -1: continue
                if livedead[i][j] < 0:
                    if livedead[i][j] == -1: livedead[i][j] = arr[i][j]
                    else: livedead[i][j] += 1
                elif livedead[i][j] > 0:
                    ci, cj = i, j
                    for dnum in range(4):
                        di, dj = dirlst[dnum]
                        ni, nj = (ci+di) % rowlen, (cj+dj) % collen
                        if arr[ni][nj] == -1 or arr[ni][nj] > 0: continue
                        if l[ni][nj] == 0:
                            l[ni][nj] = arr[ci][cj]
                            livedead[ni][nj] = -arr[ci][cj]
                        elif l[ni][nj] < arr[ci][cj]:
                            l[ni][nj] = arr[ci][cj]
                            livedead[ni][nj] = -arr[ci][cj]
                    if livedead[i][j] == 1:
                        arr[i][j] = -1
                        livedead[i][j] = 0
                    else: livedead[i][j] -= 1

        for i in range(rowlen):
            for j in range(collen):
                if l[i][j] > 0 and arr[i][j] == 0:
                    arr[i][j] = l[i][j]

    cnt = 0
    for i in range(rowlen):
        for j in range(collen):
            if livedead[i][j] != 0:
                cnt += 1
    print(f'#{tc} {cnt}')