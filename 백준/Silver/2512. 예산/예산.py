import sys
input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
arr.sort(reverse=True)
budget = int(input().rstrip())
if sum(arr) <= budget:
    print(arr[0])
else:
    limitmoney = budget//N
    answer = limitmoney
    total_arr = sum(arr)
    while limitmoney <= arr[0]:
        total = total_arr
        for num in arr:
            if num >= limitmoney:
                total -= num
                total += limitmoney
            else:
                break
        if total <= budget:
            answer = max(limitmoney, answer)
        else:
            break
        limitmoney += 1
    print(answer)