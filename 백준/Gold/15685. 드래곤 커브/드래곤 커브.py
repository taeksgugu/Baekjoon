import sys
input = sys.stdin.readline
visited = set()
N = int(input().rstrip())
dirlst = [(1,0), (0,-1), (-1,0), (0,1)]  # →, ↑, ←, ↓
for _ in range(N):
    x, y, d, g = map(int, input().rstrip().split())
    generation = 0
    dragon = [(x,y)]
    di, dj = dirlst[d]
    while generation <= g:
        if generation == 0:
            visited.add((x,y))
            if -100<=x+di<=100 and -100<=y+dj<=100:
                dragon.append((x+di, y+dj))
                visited.add((x+di, y+dj))
        else:
            standard_x, standard_y = dragon[-1]
            newdragon = []
            for a, b in dragon[:-1][::-1]:
                ni, nj = standard_x+standard_y-b, standard_y+a-standard_x
                if -100<=ni<=100 and -100<=nj<=100:
                    newdragon.append((ni,nj))
                    visited.add((ni,nj))
            dragon += newdragon
        generation += 1

answer = 0
for ci, cj in visited:
    for di, dj in [(1,0), (1,1), (0,1)]:
        ni, nj = ci+di, cj+dj
        if (ni,nj) not in visited: break
    else:
        answer += 1

print(answer)