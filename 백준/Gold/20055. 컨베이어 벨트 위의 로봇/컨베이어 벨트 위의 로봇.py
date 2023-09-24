import sys
from collections import deque
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
section = 1
cnt = 0
robot = deque()
while cnt < K:
    ### 회전
    arr = arr[-1:] + arr[:-1]
    if robot:
        for _ in range(len(robot)):
            idx = robot.popleft()
            if idx+1 < N-1:
                robot.append(idx+1)
    # print('회전', arr, robot)
    ### 로봇 이동
    if robot:
        for _ in range(len(robot)):
            idx = robot.popleft()
            if arr[idx+1] >= 1 and idx+1 not in robot:
                arr[idx+1] -= 1
                if idx+1 < N-1:
                    robot.append(idx+1)
            else:
                robot.append(idx)
    # print('이동', arr, robot)
    ### 로봇 올리기
    if arr[0] >= 1:
        arr[0] -= 1
        robot.append(0)
    # print('올리기', arr, robot)
    # print()
    cnt = arr.count(0)
    section += 1
print(section-1)