import sys
from collections import deque
input = sys.stdin.readline

### 입력 받기
M, S = map(int, input().split())
fishlst = [list(map(lambda x: int(x)-1, input().split())) for _ in range(M)]
si, sj = map(lambda x: int(x)-1, input().split()) ### 상어 위치
smellarr = {}
### 방향리스트
dirlst = [(0,-1), (-1,-1), (-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1)] # ←, ↖, ↑, ↗, →, ↘, ↓, ↙
sharkdir = {'1':(-1,0), '2':(0,-1), '3':(1,0), '4':(0,1)} # 1:상, 2:좌, 3:하, 4: 우

### 상어가 3칸 이동하면서 제외되는 물고기 수가 가장 많은 방법 찾는 함수
howtogo = []
def makeshark(lst):
    if len(lst) == 3:
        howtogo.append(lst)
        return
    for i in range(1,5):
        makeshark(lst+str(i))

makeshark('')

for roundnum in range(1, S+1):
    # print(roundnum)
    # 상어가 모든 물고기에게 복제 마법을 시전한다. 복제 마법은 시간이 조금 걸리기 때문에, 아래 5번에서 물고기가 복제되어 칸에 나타난다.
    fishcopy = [e[:] for e in fishlst] ### 복제 리스트
    ### 디버깅
    # for l in fishcopy:
    #     print(*l)
    # 모든 물고기가 한 칸 이동한다
    aftermovefish = []
    for fi,fj,fd in fishlst:
        flag = False
        for _  in range(8):
            di, dj = dirlst[fd]
            ni, nj = fi+di, fj+dj
            if ni<0 or ni>=4 or nj<0 or nj>=4 or ((ni,nj) in smellarr and smellarr[(ni,nj)]>0) or (si==ni and sj==nj): fd = (fd-1)%8
            else:
                flag = True
                aftermovefish.append((ni,nj,fd))
                break
        if not flag: ### 다 회전해도 갈 곳이 없다면 움직이지 않는다.
            aftermovefish.append((fi,fj,fd))

    ### 디버깅
    # print('이동후')
    # print(aftermovefish)

    # 상어가 연속해서 3칸 이동한다. 상어는 현재 칸에서 상하좌우로 인접한 칸으로 이동할 수 있다. 연속해서 이동하는 칸 중에 격자의 범위를 벗어나는 칸이 있으면, 그 방법은 불가능한 이동 방법이다. 연속해서 이동하는 중에 상어가 물고기가 있는 같은 칸으로 이동하게 된다면, 그 칸에 있는 모든 물고기는 격자에서 제외되며, 제외되는 모든 물고기는 물고기 냄새를 남긴다. 가능한 이동 방법 중에서 제외되는 물고기의 수가 가장 많은 방법으로 이동하며, 그러한 방법이 여러가지인 경우 사전 순으로 가장 앞서는 방법을 이용한다. 사전 순에 대한 문제의 하단 노트에 있다.
    ### 상어가 확인할 배열 만들기
    fisharr = [[[] for _ in range(4)] for _ in range(4)]
    for fi,fj,fd in aftermovefish:
        fisharr[fi][fj].append(fd)
    ### 디버깅
    # print('물고기 배열')
    # for l in fisharr:
    #     print(*l)
    # print(si,sj)
    routecnt, route = 0, '444'
    for howshar in howtogo:
        visited = [[0]*4 for _ in range(4)]
        nsi, nsj = si, sj
        cnt = 0
        flag = False
        for rdnum in howshar:
            di, dj = sharkdir[rdnum]
            nsi, nsj = nsi + di, nsj + dj
            if nsi<0 or nsi>=4 or nsj<0 or nsj>=4:
                flag = True
                break

            if fisharr[nsi][nsj]:  ### 지나가는 칸에 물고기가 있다면
                # print(nsi,nsj, fisharr[nsi][nsj])
                if visited[nsi][nsj] == 0:
                    cnt += len(fisharr[nsi][nsj])
                    visited[nsi][nsj] = 1


        if not flag:
            # print(cnt, howshar)
            if cnt > routecnt:
                routecnt, route = cnt, howshar
            elif cnt == routecnt:
                routecnt, route = sorted([(routecnt, route), (cnt, howshar)], key=lambda x: (-x[0], int(x[1])))[0]

    ### 디버깅
    # print('상어 이동 가능 위치 확인')
    # print('선택 경로', routecnt, route)

    # 두 번 전 연습에서 생긴 물고기의 냄새가 격자에서 사라진다.
    ### 이걸 위에 냄새 남기고 하면 꼬이기 때문에 이것 부터 시전
    for (i,j) in smellarr:
            if smellarr[(i,j)] > 0: smellarr[(i,j)] -= 1
    ### 해당 경로 물고기 제거 및 냄새 남기기
    for rdnum in route:
        # di, dj = sharkdir[int(rdnum)]
        di, dj = sharkdir[rdnum]
        # print(rdnum, si, sj, '에서', si + di, sj + dj)
        si, sj = si+di, sj+dj
        if fisharr[si][sj]: ### 지나가는 칸에 물고기가 있다면
            fisharr[si][sj] = [] ### 다 제거
            smellarr[(si,sj)] = 2 ### 냄새 남기기

    ### 디버깅
    # print('물고기 제거 및 냄새 확인')
    # for l in fisharr:
    #     print(*l)
    # print('냄새')
    # for l in smellarr:
    #     print(l, smellarr[l])

    # 1에서 사용한 복제 마법이 완료된다. 모든 복제된 물고기는 1에서의 위치와 방향을 그대로 갖게 된다.
    for i in range(4):
        for j in range(4):
            if fisharr[i][j]: ### 상어 지나가고 물고기 남았으면
                for fd in fisharr[i][j]:
                    fishcopy.append([i,j,fd])

    fishlst = [e[:] for e in fishcopy]
    # print('물고기 확인')
    # print(si,sj)
    # print(fishlst)
    # debug = [[[] for _ in range(4)] for _ in range(4)]
    # for fi,fj,fd in fishlst:
    #     debug[fi][fj].append(fd)
    # for l in debug:
    #     print(*l)
    # print()
print(len(fishlst))