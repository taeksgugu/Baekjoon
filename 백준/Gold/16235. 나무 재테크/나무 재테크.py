import sys
# from collections import deque
input = sys.stdin.readline
N, M, K = map(int, input().rstrip().split())
### 나무 리스트 생각하는 파트
land = [[[] for _ in range(N)] for _ in range(N)]
### 처음에 양분은 5씩 들어감
energy = [[5] * N for _ in range(N)]
### 매년 겨울 S2D2가 추가할 양분
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]
for _ in range(M):
    x, y, z = map(int, input().rstrip().split())
    land[x-1][y-1].append(z)
### 입력 끝
year = 1
while year<=K:
    ### 봄
    for i in range(N):
        for j in range(N):
            if land[i][j]: ### 나무가 있다면
                land[i][j].sort() ## 어린 나이부터 양분 섭취
                current_energy = energy[i][j] ## 현재 그 칸의 양분
                newlst = [] ### 양분 섭취하고 추가될 나무 리스트
                while land[i][j]:
                    tree = land[i][j].pop(0)
                    if current_energy < tree:
                        land[i][j].append(tree)
                        break
                    else:
                        current_energy -= tree
                        newlst.append(tree+1)
                remainlst = land[i][j] ### 죽은 나무 리스트
                land[i][j] = newlst  ### 성장한 나무 리스트 갱신
                energy[i][j] = current_energy ### 남은 양분 갱신
    ### 여름 -> 죽은 나무 리스트는 애초에 나무가 있었어야했기 때문에 위에서 계속 이어서 진행
                for remain_tree in remainlst:
                    energy[i][j] += remain_tree//2
    ### 가을 -> 다시 이중 for문을 돌리는 이유는 나무가 번식하면서 다른 칸에 영향을 주기 때문
    for i in range(N):
        for j in range(N):
            if land[i][j]: ## 나무가 있어야 번식 가능
                ### 나이가 5의 배수인 나무 수만큼 주변 8칸에 번식하기 때문
                num = len([x for x in land[i][j] if x%5==0])
                for di, dj in [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1)]:
                    ni,nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N:
                        land[ni][nj].extend([1]*num) ### 나무 수만큼 나이가 1인 나무가 생김
    ### 겨울 -> 양분 추가 굳이 나눌 필요 없어서 같이 진행
            energy[i][j] += arr[i][j]
    # print(year)
    year += 1
    # for l in land:
    #     print(l)
    # print()
print(sum([len(x) for y in land for x in y]))