import sys
from collections import deque
input = sys.stdin.readline

N, M, energy = map(int, input().rstrip().split())
arr = [list(map(int, input().rstrip().split())) for _ in range(N)]

si, sj = map(lambda x: int(x)-1, input().split())

passengerdic = {}
for i in range(1, M+1):
    data = list(map(lambda x: int(x)-1, input().split()))
    passengerdic[(data[0], data[1])] = (data[2], data[3])

# print(passengerdic)

def solve():
    global si, sj, energy
    for _ in range(M):
        if energy == 0: return -1 ### 시작 안됨
        ### 출발
        if (si,sj) not in passengerdic: ### 해당자리에 승객이 없다면?
            visited = [[0]*N for _ in range(N)]
            q = deque()
            q.append((si,sj))
            visited[si][sj] = energy
            find = False
            while q:
                findlst = []
                for _ in range(len(q)):
                    i, j = q.popleft()
                    remain = visited[i][j] -1
                    if (i,j) in passengerdic:
                        find = True
                        findlst.append((i,j))
                        break
                    for di, dj in [(-1,0), (0,-1), (0,1), (1,0)]:
                        ni, nj = i+di, j+dj
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 0 and visited[ni][nj] == 0:
                            visited[ni][nj] = remain
                            q.append((ni,nj))
                            if (ni,nj) in passengerdic:
                                findlst.append((ni,nj))
                                find = True
                if remain == 0:
                    print('승객 찾다가 연료 부족')
                    for l in visited:
                        print(*l)
                    return -1### 연로 다썼따면
                if find: break
            if not find: return -1 ### 못 간다면...
            findlst.sort(key=lambda x: (x[0], x[1]))
            si, sj = findlst[0]
            energy = visited[si][sj]
        # else:
        #     print('그자리에 있음')

        # print('승객 찾음', si, sj, '에너지', energy)
        #
        # for l in visited:
        #     print(*l)

        ### 목적지 가기
        visited =[[0]*N for _ in range(N)]
        q = deque()
        q.append((si,sj))
        ai, aj = passengerdic[(si,sj)] ### 목표지점
        visited[si][sj] = energy
        beforeenergy = energy
        find = False
        while q:
            for _ in range(len(q)):
                i, j = q.popleft()
                remain = visited[i][j]-1
                for di, dj in [(-1,0), (0,-1), (0,1), (1,0)]:
                    ni, nj = i+di, j+dj
                    if 0<=ni<N and 0<=nj<N and arr[ni][nj]==0 and visited[ni][nj]==0:
                        visited[ni][nj] = remain
                        q.append((ni,nj))
                        if ni == ai and nj == aj:
                            find = True
                            # print('목적지 찾음', i,j,'에서', '에너지', visited[ni][nj])
                            del passengerdic[(si,sj)] ### 해당 승객 제거
                            si, sj = ai, aj
                            # print('목적지', si,sj)
                            break
                if find: break
            if find: break
            if remain == 0:
                # print('연료 부족으로 목적지 못 감')
                # for l in visited:
                #     print(*l)
                return -1

        if not find: return -1
        energy = visited[si][sj] + (beforeenergy-visited[si][sj])*2
        # print('남은 에너지', energy)

    return energy

print(solve())