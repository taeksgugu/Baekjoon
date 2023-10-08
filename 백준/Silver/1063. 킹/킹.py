import sys, heapq
input = sys.stdin.readline

K, STONE, N = input().split()
alphabet = list('0ABCDEFGH')
def makepos(word):
    wi = int(word[1])
    wj = alphabet.index(word[0])
    return wi, wj
dirlst ={'R': (0,1), 'L': (0,-1), 'B': (-1,0), 'T': (1,0),
         'RT': (1,1), 'LT': (1,-1), 'RB': (-1,1), 'LB': (-1,-1)}
ki, kj = makepos(K)
si, sj = makepos(STONE)
for _ in range(int(N)):
    order = input().replace('\n','')
    di, dj = dirlst[order]
    ni, nj = ki+di, kj+dj
    if ni<1 or ni>=9 or nj<1 or nj>=9: continue
    else:
        if (ni, nj) == (si, sj):
            nsi, nsj = si+di, sj+dj
            if nsi<1 or nsi>=9 or nsj<1 or nsj>=9: continue
            else: si, sj = nsi, nsj
        ki, kj = ni, nj
print(alphabet[kj]+str(ki))
print(alphabet[sj]+str(si))