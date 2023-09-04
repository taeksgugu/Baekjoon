import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
### 좌표 조정 함수 만들기 (다 연결되기 때문)
def control(i):
    if i < 0:
        if (-1)*i % N == 0:
            return 0
        else:
            return i + ((-1) * i // N + 1) * N
    elif 0<=i<N:
        return i
    else:
        return i % N
### 방향 리스트 만들기 ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dirlst = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)]

### 처음 비바라기 시전
cloudlst = [(N-1,0), (N-1,1), (N-2,0), (N-2,1)]

### M번 명령하기
for _ in range(M):
    di, si = map(int, input().rstrip().split())
    di, dj = map(lambda x: x*si, dirlst[di-1])
    ### di 방향으로 si칸 이동 & 구름 있는 칸 바구니의 물 양 증가
    check = set()
    while cloudlst:
        i, j = cloudlst.pop()
        ci, cj = control(i+di), control(j+dj)
        check.add((ci,cj))
        arr[ci][cj] += 1

    ### 구름 사라짐 -> 나중에 사라진 칸 체크를 위해 남겨놓음
    ### 2에서 물이 증가한 칸 물복사 시전
    for cloud_i, cloud_j in check:
        cnt = 0
        for ki, kj in [(-1,-1), (-1,1), (1,-1), (1,1)]:
            ni, nj = cloud_i+ki, cloud_j+kj
            if 0<=ni<N and 0<=nj<N and arr[ni][nj] > 0:
                cnt += 1
        arr[cloud_i][cloud_j] += cnt

    ### 2이상인 칸 구름 생성
    for i in range(N):
        for j in range(N):
            if (i,j) not in check and arr[i][j] >=2:
                cloudlst.append((i,j))
                arr[i][j] -= 2

print(sum(x for y in arr for x in y))