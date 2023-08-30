import sys
input = sys.stdin.readline
idxdict = {'A':'1', 'B':'2', 'C':'3', 'D':'4', 'E':'5', 'F':'6'}
def checkknight(before, after):
    ### 가로차 2 세로차 1
    if (abs(int(before[0])-int(after[0])) == 2 and abs(int(before[1])-int(after[1])) == 1)\
        or (abs(int(before[0])-int(after[0])) == 1 and abs(int(before[1])-int(after[1])) == 2):
        return True
    return False
arr = [input().rstrip() for _ in range(36)]
def knighttour(arr):
    global before, after, start
    if len(arr) != len(set(arr)):
        return 'Invalid'
    for i in range(36):
        if i == 0:
            start = arr[i]
            start = start.replace(start[0], idxdict[start[0]])
            before = start[::]
            # visited[int(start[0])-1][int(start[1])-1] = 1
            # print(start)
        else:
            after = arr[i]
            after = after.replace(after[0], idxdict[after[0]])
            # if visited[int(after[0])-1][int(after[1])-1] == 1:
            #     print('이미 방문', after, before)
            #     return 'Invalid'
            if not checkknight(before, after):
                # print('나이트 이동 x', after, before)
                return 'Invalid'
            before = after
            if i == 35:
                if not checkknight(after, start):
                    return 'Invalid'
    return 'Valid'
print(knighttour(arr))