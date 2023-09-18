T = int(input())
# T = 1
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    corelst = []
    startcnt, othercnt = 0, 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if i == 0 or i == N - 1 or j == 0 or j == N - 1:
                    startcnt += 1
                else:
                    othercnt += 1
                    corelst.append((i, j))

    coredic = {}
    dirlst = [(0,1), (0,-1), (1,0), (-1,0)] ### 0:동, 1:서, 2:남, 3:북
    for ci, cj in corelst:
        for i in range(4):
            di, dj = dirlst[i]
            k = 1
            while True:
                ni, nj = ci + di * k, cj + dj * k
                if 0 <= ni < N and 0 <= nj < N:
                    if arr[ni][nj] == 0: k += 1
                    elif arr[ni][nj] == 1 or arr[ni][nj] == 2: break
                elif ni < 0 or ni >= N or nj < 0 or nj >= N:
                    try: coredic[(ci,cj)].append((i,k-1))
                    except: coredic[(ci,cj)] = [(i,k-1)]
                    break

    finalcnt, finallength = 0, 0
    def process(n, idx, length):
        global finallength, finalcnt
        if n>finalcnt:
            finalcnt = n
            finallength = length
        elif n == finalcnt:
            finallength = min(length, finallength)

        if n == othercnt:
            return

        for i in range(idx+1, othercnt):
            ci, cj = corelst[i]
            if (ci,cj) in coredic:
                for cdir, clength in coredic[(ci,cj)]:
                    di, dj = dirlst[cdir]
                    for kk in range(1, clength+1):
                        if arr[ci+di*kk][cj+dj*kk] == 2: break
                    else:
                        for kk in range(1, clength + 1):
                            arr[ci+di*kk][cj+dj*kk] = 2
                        process(n+1, i, length+clength)
                        for kk in range(1, clength + 1):
                            arr[ci+di*kk][cj+dj*kk] = 0
        # process(n, idx+1, length)
    process(0,-1,0)
    print(f"#{tc} {finallength}")