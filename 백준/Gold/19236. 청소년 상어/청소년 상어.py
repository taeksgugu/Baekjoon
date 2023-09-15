### 이문제를 재귀... 진짜 어렵네 아직 숙련도가 딸리는 듯
import sys
input = sys.stdin.readline
### 입력 받기
si, sj, sdir = 0, 0, 0 ### 상어 시작 좌표 및 방향
totalscore = 0
fishpos = [() for _ in range(17)]
fishdir = [-1 for _ in range(17)]
for i in range(4):
    lineinfo = list(map(int, input().split()))
    for j in range(0,4):
        if i==0 and j==0:
            sdir = lineinfo[j*2+1]-1
            totalscore = lineinfo[j*2]
            fishpos[lineinfo[j*2]] = () ### 물고기 시작부터 먹힘
            fishdir[lineinfo[j*2]] = -1 ### 방향도 없어짐
        else:
            fishpos[lineinfo[j*2]] = (i,j)
            fishdir[lineinfo[j*2]] = lineinfo[j*2+1]-1
#
# print(si,sj,sdir)
# print(fishpos)
# print(fishdir)

### 방향리스트
dirlst = [(-1,0), (-1,-1), (0,-1), (1,-1), (1,0), (1,1), (0,1), (-1,1)] # ↑, ↖, ←, ↙, ↓, ↘, →, ↗
answer = 0
### 완전탐색으로 진행함
def solve(si, sj, sdir, totalscore, fishpos, fishdir): ### 상어 위치, 방향, 먹은번호합, 물고기 위치 방향 받아오기
    global answer
    newpos = [e[:] for e in fishpos]
    # newdir = [-1 for _ in range(17)]
    newdir = [e for e in fishdir] # fishdir[:]
    arr = {newpos[num]:num for num in range(1,17)} ### 함수 내에서 빠르게 확인할 물고기 위치 딕셔너리 만들기
    # print('물고기 이동 전', si, sj, totalscore)
    # print(newpos)
    # print(newdir)
    # newarr = [[0] * 4 for _ in range(4)]
    # for k, v in arr.items():
    #     if k:
    #         newarr[k[0]][k[1]] = v
    # for vv in newarr:
    #     print(vv)
    # print()

    for num in range(1,17): ### 물고기 번호 순대로 이동
        if newpos[num]: ### 해당 물고기가 아직 안 잡혀먹혔다면
            fi, fj = newpos[num]
            fdir = newdir[num]
            di, dj = dirlst[fdir]
            ni, nj = fi+di, fj+dj
            if (ni<0 or ni>=4 or nj<0 or nj>=4) or (ni==si and nj==sj): ### 밖으로 나가거나 상어칸인 경우
                cnt = 1
                for ndi, ndj in (dirlst[fdir + 1:] + dirlst[:fdir]):  ### 반시계 45도 회전
                    ni2, nj2, ndir = fi + ndi, fj + ndj, (fdir + cnt) % 8
                    if 0 <= ni2 < 4 and 0 <= nj2 < 4 and not (ni2 == si and nj2 == sj):  ### 갈 수 있다면 and arr[ni][nj] != 'shark' 이건 생략
                        ni, nj, fdir = ni2, nj2, ndir  ### 이동할 칸으로 변경하고 방향도 변경
                        # print(num, ni2, nj2, fdir, ndir)
                        break
                    cnt += 1
                else:
                    newdir[num] = ndir
                    continue ### 그냥 유지
            if 0<=ni<4 and 0<=nj<4: ### 공간 안으로 들어옴 상어도 아님 상어는 위에서 거름
                if (ni,nj) not in arr or not arr[(ni,nj)]: ### arr에 없다는건 물고기가 있는 칸이 아니란 말! 0일 경우는 원래 있던 물고기가 다른 칸으로 이동해서 빈칸일수도 있음
                    newpos[num] = (ni,nj)### 물고기 위치 바꾸기
                    newdir[num] = fdir ### 물고기 방향 유지하기
                    arr[(ni,nj)] = num ### 현재 arr에 추가하거나 갱신하기
                    arr[(fi,fj)] = 0
                elif (ni,nj) in arr and arr[(ni,nj)] != 0: ### 해당칸에 물고기가 있을 경우
                    changenum = arr[(ni,nj)] ### 자리바꿀 물고기 번호
                    newpos[changenum], newpos[num] = (fi,fj), (ni,nj)### 원래 물고기랑 자리 바꾸기
                    newdir[num] = fdir
                    arr[(ni,nj)], arr[(fi,fj)] = num, changenum ### arr도 갱신
    # print('물고기 이동 끝')
    # print(newpos)
    # print(newdir)
    # newarr = [[0]*4 for _ in range(4)]
    # for k, v in arr.items():
    #     if k:
    #         newarr[k[0]][k[1]] = v
    # for vv in newarr:
    #     print(vv)
    # print()
    ### 상어 이동 시작
    sdi, sdj = dirlst[sdir]
    for sk in range(1,4): ## 최대 3번 (끝에 있을 때)
        sni, snj = si+sdi*sk, sj+sdj*sk
        if sni<0 or sni>=4 or snj<0 or snj>=4: ### 공간을 벗어난다는건 더 갈 일 없다는 뜻
            answer = max(answer, totalscore)
            # print(si, sj,'끝')
            return
        if 0<=sni<4 and 0<=snj<4: ### 공간 안
            if (sni,snj) not in arr or not arr[(sni,snj)]: continue ### 물고기가 해당칸에 없는 경우
            if (sni,snj) in arr and arr[(sni,snj)] != 0: ### 물고기가 있다면
                fishnum = arr[(sni,snj)] ### 잡아먹히는 물고기 번호
                newsdir = newdir[fishnum] ### 상어의 새 방향
                newpos[fishnum] = () ### 물고기 잡아먹기
                newdir[fishnum] = -1### 물고기 pos랑 dir 없애기
                ### 상어 위치 갱신 / 상어 방향 갱신 / 점수 합산
                solve(sni, snj, newsdir, totalscore+fishnum, newpos, newdir)
                newpos[fishnum] = (sni,snj)  ### 물고기 되돌아오기
                newdir[fishnum] = newsdir  ### 물고기 pos랑 dir 되돌리기
solve(si, sj, sdir, totalscore, fishpos, fishdir)
print(answer)