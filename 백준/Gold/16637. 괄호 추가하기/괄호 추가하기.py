import sys
from collections import deque

input = sys.stdin.readline
N = int(input())
lst = list(input().rstrip())

def calculate(lst):
    result = False  ### 초기 상태
    idx = 0
    while idx<len(lst):
        s = lst[idx]
        # print(idx,s)
        if s.isnumeric():
            if not result: ### 첫 숫자일 경우
                result = int(s)
            idx += 1
        elif s in ['+','-','*']:
            if lst[idx+1] != '(': # 다음에 괄호가 오지 않으면
                if s == '+': result += int(lst[idx+1])
                elif s == '-': result -= int(lst[idx+1])
                else: result *= int(lst[idx+1])
                idx += 2
            else: ### 괄호라면 먼저 계산
                num1, cal, num2 = lst[idx+2:idx+5]
                if cal == '+': num = int(num1) + int(num2)
                elif cal == '-': num = int(num1) - int(num2)
                else: num = int(num1) * int(num2)

                if s == '+': result += num
                elif s == '-': result -= num
                else: result *= num
                idx += 6
        else: ###'('라면
            num1, cal, num2 = lst[idx + 1:idx + 4]
            if cal == '+':
                num = int(num1) + int(num2)
            elif cal == '-':
                num = int(num1) - int(num2)
            else:
                num = int(num1) * int(num2)
            result = num
            idx += 5
    return result

answer = -float('INF')
def makecomb(n, callst):
    global answer
    # print(n, callst)
    newlst = lst[:]
    for i in callst[::-1]:
        if i % 2 == 0:
            newlst.insert(i, '(')
        else:
            newlst.insert(i, ')')
    newval = calculate(newlst)
    answer = max(answer, newval)
    # print(''.join(newlst), newval)
    for i in range(n + 1, N):
        if lst[i].isnumeric() and i + 2 <= N:
            makecomb(i + 2, callst + [i, i + 3])


makecomb(-1, [])
print(answer)