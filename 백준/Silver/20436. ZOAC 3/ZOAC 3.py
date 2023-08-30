import sys
input = sys.stdin.readline
leftdict = {'q': [0,0], 'w': [0,1], 'e': [0,2], 'r': [0,3], 't': [0,4], 'a': [1,0], 's': [1,1], 'd': [1,2], 'f': [1,3],'g':[1,4], 'z': [2,0], 'x': [2,1], 'c': [2,2], 'v': [2,3]}
rightdict = {'y': [0,5], 'u': [0,6], 'i': [0,7], 'o': [0,8], 'p': [0,9], 'h': [1,5], 'j': [1,6], 'k': [1,7], 'l': [1,8],'b': [2,4], 'n': [2,5], 'm': [2,6]}
a, b = input().rstrip().split()
left, right = leftdict[a], rightdict[b]
word = input().rstrip()
answer = 0
for w in word:
    answer += 1
    if w in leftdict:
        before_x, before_y = left[0], left[1]
        now_x, now_y = leftdict[w][0], leftdict[w][1]
        answer += (abs(before_x-now_x)+abs(before_y-now_y))
        left = leftdict[w]
    else:
        before_x, before_y = right[0], right[1]
        now_x, now_y = rightdict[w][0], rightdict[w][1]
        answer += (abs(before_x-now_x)+abs(before_y-now_y))
        right = rightdict[w]
print(answer)