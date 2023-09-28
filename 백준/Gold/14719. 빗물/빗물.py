import sys
input = sys.stdin.readline
### 입력 받기
H, W = map(int, input().split())
lst = list(map(int, input().split()))
water = 0
for num in range(1,W-1):
    left = max(lst[:num])
    right = max(lst[num+1:])
    height = lst[num]
    if height <= min(left, right):
        water += (min(left,right) - height)

print(water)