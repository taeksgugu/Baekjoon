### 초기 풀이 과정 : 로봇 좌표를 리스트로 관리
###               다른 문제들과는 다르게 좌표를 보는 방식이 다르고, 좌표 축 순서도 달라서 조심해야함

import sys
input = sys.stdin.readline

A, B = map(int, input().rstrip().split())
N, M = map(int, input().rstrip().split())

dirdic = {'N':0, 'W':1, 'S':2, 'E':3} ### 입력시 변경할 예정
dirlst = [(0,1), (-1,0), (0,-1), (1,0)] ### N W S E 순으로 넣음
robotlst = [[] for _ in range(N+1)]
position = {}
for num in range(1, N+1):
    robotdata = input().split()
    robotlst[num] = [int(robotdata[0])-1, int(robotdata[1])-1, dirdic[robotdata[2]]]
    position[(int(robotdata[0])-1, int(robotdata[1])-1)] = num
orderlst = [input().split() for _ in range(M)]
def simulation():
    for orderdata in orderlst:
        robotnum = int(orderdata[0])
        order = orderdata[1]
        for _ in range(int(orderdata[-1])):
            if order == 'L':
                robotlst[robotnum][2] = (robotlst[robotnum][2]+1)%4
            elif order == 'R':
                robotlst[robotnum][2] = (robotlst[robotnum][2]-1) % 4
            else:
                ri, rj, rdir = robotlst[robotnum]
                di, dj = dirlst[rdir]
                ni, nj = ri+di, rj+dj
                if ni<0 or ni>=A or nj<0 or nj>=B:
                    print(f"Robot {robotnum} crashes into the wall")
                    return
                if 0<=ni<A and 0<=nj<B:
                    if (ni,nj) in position:
                        print(f"Robot {robotnum} crashes into robot {position[(ni,nj)]}")
                        return
                    else:
                        robotlst[robotnum] = [ni,nj,rdir]
                        position[(ni,nj)] = robotnum
                        del position[(ri,rj)]
    print('OK')
    return

simulation()
