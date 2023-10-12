import heapq, sys
input = sys.stdin.readline

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

visited = [[1e9]*W for _ in range(H)]
dirlst = [(-1,0), (1,0), (0,-1), (0,1)]

def dijkstra():
    q = [(0,ti,tj)]
    heapq.heapify(q)
    visited[ti][tj] = 0
    while q:
        cur_dist, ci,cj = heapq.heappop(q)
        if arr[ci][cj] == 'E':
            return cur_dist

        for di, dj in dirlst:
            k = 1
            dist = cur_dist
            while True:
                ni, nj = ci+di*k, cj+dj*k
                if ni<0 or ni>=H or nj<0 or nj>=W or arr[ni][nj] == 'H': break
                if arr[ni][nj] == 'E':
                    heapq.heappush(q, (dist, ni, nj))
                    break
                if arr[ni][nj] == 'R':
                    if visited[ni-di][nj-dj]>dist:
                        visited[ni-di][nj-dj] = dist
                        heapq.heappush(q, (dist, ni-di, nj-dj))
                    break
                else:
                    k += 1
                    dist += int(arr[ni][nj])

    return -1
print(dijkstra())