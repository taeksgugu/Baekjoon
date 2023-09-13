import sys
input = sys.stdin.readline

def makeword(n, word):
    if n == wordlen:
        resultlst.add(word)
        return
    for i in worddic:
        if worddic[i]:
            worddic[i] -= 1
            makeword(n+1, word+i)
            worddic[i] += 1

T = int(input().rstrip())
for _ in range(T):
    word = sorted(list(input().rstrip()))
    wordlen = len(word)
    worddic = {}
    for w in word:
        try: worddic[w] += 1
        except: worddic[w] = 1
    resultlst = set()
    makeword(0,'')
    for res in sorted(list(resultlst)):
        print(res)