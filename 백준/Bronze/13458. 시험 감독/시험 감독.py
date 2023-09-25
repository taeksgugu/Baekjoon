N = int(input())
lst = list(map(int, input().split()))
B, C = map(int, input().split())

answer = 0

for num in lst:
    answer += 1
    if num <=B : continue
    else:
        num -= B

    if num%C == 0: answer += num//C
    else: answer += (num//C)+1
    # print(answer)
print(answer)