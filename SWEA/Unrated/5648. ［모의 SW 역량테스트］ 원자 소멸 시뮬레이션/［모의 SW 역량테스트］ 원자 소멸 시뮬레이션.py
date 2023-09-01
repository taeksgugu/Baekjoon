dirlst = [(0, 1), (0, -1), (-1, 0), (1, 0)]
T = int(input())
for tc in range(1, T+1):

    answer = 0
    N = int(input())
    arr = []
    for _ in range(N):
        i, j, dir, energy = map(int, input().split())
        i, j = (i+1000)*2, (j+1000)*2
        arr.append([i,j, dir, energy])
    while arr:
        ### 0.5 씩 이동 후 해당 좌표 확인
        deletelst = [] ### 정해진 지도 밖으로 나가는 리스트
        visited = {}
        for idx in range(len(arr)):
            i, j, dir, energy = arr[idx]
            di, dj = dirlst[dir]
            ni, nj = i+di, j+dj
            if ni<0 or ni>=4001 or nj<0 or nj>=4001:
                deletelst.append(idx)
            else:
                if (ni,nj) in visited:
                    visited[(ni,nj)] += 1
                else:
                    visited[(ni,nj)] = 1
            arr[idx][0], arr[idx][1] = ni, nj
        finalarr = []
        for meet_idx in range(len(arr)):
            if meet_idx not in deletelst:
                ci, cj, cdir, cenergy = arr[meet_idx]
                if visited[(ci,cj)] >= 2:
                    answer += cenergy
                else:
                    finalarr.append(arr[meet_idx])
        arr = finalarr
    print(f"#{tc} {answer}")