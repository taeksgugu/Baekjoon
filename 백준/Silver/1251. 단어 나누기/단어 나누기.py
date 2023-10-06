import sys
input = sys.stdin.readline

word = input().rstrip()
N = len(word)
totallst = []
def makecomb(idx, lst):
    if len(lst)==2:
        newlst = word[:lst[0]+1][::-1] + word[lst[0]+1:lst[1]+1][::-1] + word[lst[1]+1:][::-1]
        totallst.append(newlst)
        return

    for i in range(idx+1, N-1):
        makecomb(i, lst+[i])

makecomb(-1,[])
totallst.sort()
print(totallst[0])