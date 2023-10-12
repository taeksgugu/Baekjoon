W, H = map(int, input().split())
arr = [list(input()) for _ in range(H)]

flag = False
for i in range(H):
    for j in range(W):
        if arr[i][j]=='T':
            ti, tj = i, j
            flag = True
            arr[ti][tj] = '0'
            break
    if flag: break

visited = [[[-1]*W for _ in range(H)] for _ in range(4)]
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]
cango = [[2,3], [2,3], [0,1], [0,1]]
import heapq
def dijkstra():

    q = [(0,0,ti,tj),(0,1,ti,tj),(0,2,ti,tj),(0,3,ti,tj)]
    heapq.heapify(q)
    answer = 1e9
    for i in range(4):
        visited[i][ti][tj] = 0
    while q:
        cur_cnt,cur_d, ci,cj = heapq.heappop(q)
        if arr[ci][cj] == 'E':
            return answer
        di, dj = dirlst[cur_d]
        k = 1
        dist = cur_cnt
        while True:
            ni, nj = ci+di*k, cj+dj*k
            if ni<0 or ni>=H or nj<0 or nj>=W or arr[ni][nj] == 'H': break
            if arr[ni][nj] == 'E':
                # print('찾음')
                answer = min(answer, dist)
                heapq.heappush(q, (dist, cur_d, ni, nj))
                break
            if arr[ni][nj] == 'R':
                for idx in cango[cur_d]:
                    if visited[idx][ni-di][nj-dj]==-1 or visited[idx][ni-di][nj-dj]>dist:
                        visited[idx][ni-di][nj-dj] = dist
                        heapq.heappush(q, (dist, idx, ni-di, nj-dj))
                break
            else:
                k += 1
                dist += int(arr[ni][nj])

    if answer == 1e9: return -1
    else: return answer
print(dijkstra())