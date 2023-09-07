import sys
input = sys.stdin.readline
N = input().rstrip()
length = len(N)
N = int(N)
if length == 1:
    print(N)
elif length == 2:
    print(9+(N-9)*2)
else:
    print(int(str(length-2)+'8'*(length-2)+'9') + (N-int('9'*(length-1)))*length)