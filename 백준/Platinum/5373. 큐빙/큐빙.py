'''
초기 풀이 과정: 진짜 더럽고 더럽고 더러운 문제다. 이걸 기출로 냈다니... 너무한 문제다.
              최근에 주사위 굴리기 등 문제를 많이 풀어서 dice로 만들어서 하려고 했는데... 너무 코드가 복잡하고 디버깅도 힘들었다.
              (한번 삐끗해서... 다 지우고 다시 작성함)
              도저히 시계와 반시계를 나누기가 너무 귀찮았음... 그래서 반시계는 시계의 3번이라고 생각하고 진행함 (물론 시간은 더 걸리겠지만...)
              일단 해봄 (테이블 만드느라 한번 죽을 뻔했음)

과정 피드백 : 중간에 한번 삐끗햇던 기억에... 무조건 번호를 순서대로 정렬해서 선언함
            이게 한줄한줄 바꾸다보면,,, 순서도 매우 중요함 (잘못하면 꼬임...)
            디버깅하다가 죽을 뻔함...
            디버깅 코드는 보통 지우는데 이건 너무 아까워서 남김... ㅎㅎ
'''
import sys
input = sys.stdin.readline
### 입력 받기
T = int(input())
for _ in range(T):
    n = int(input())
    orderlst = input().split()
    ### 문제 설명대로 큐브 6면 만들기 
    up = [['w' for _ in range(3)] for _ in range(3)]
    down = [['y' for _ in range(3)] for _ in range(3)]
    front = [['r' for _ in range(3)] for _ in range(3)]
    back = [['o' for _ in range(3)] for _ in range(3)]
    left = [['g' for _ in range(3)] for _ in range(3)]
    right = [['b' for _ in range(3)] for _ in range(3)]
    ### 명령 수행
    for order in orderlst:
        square, direction = order[0], order[1]
        ### 시계 방향으로 몇번 돌릴지 확인, '+'면 1번, '-'면 3번
        if direction == '+': turns = 1
        else: turns = 3
        if square == 'U':
            for _ in range(turns):
                up[0][0], up[0][1], up[0][2], up[1][2], up[2][2], up[2][1], up[2][0], up[1][0] = up[2][0], up[1][0], up[0][0], up[0][1], up[0][2], up[1][2], up[2][2], up[2][1]
                front[0][0], front[0][1], front[0][2], right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2] = right[0][0], right[0][1], right[0][2], back[0][0], back[0][1], back[0][2], left[0][0], left[0][1], left[0][2], front[0][0], front[0][1], front[0][2]
        elif square == 'D':
            for _ in range(turns):
                down[0][0], down[0][1], down[0][2], down[1][2], down[2][2], down[2][1], down[2][0], down[1][0] = down[2][0], down[1][0], down[0][0], down[0][1], down[0][2], down[1][2], down[2][2], down[2][1]
                front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2], left[2][0], left[2][1], left[2][2] = left[2][0], left[2][1], left[2][2], front[2][0], front[2][1], front[2][2], right[2][0], right[2][1], right[2][2], back[2][0], back[2][1], back[2][2]
        elif square == 'F':
            for _ in range(turns):
                front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1], front[2][0], front[1][0] = front[2][0], front[1][0], front[0][0], front[0][1], front[0][2], front[1][2], front[2][2], front[2][1]
                right[0][0], right[1][0], right[2][0], up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[2][0], down[2][1], down[2][2] = up[2][0], up[2][1], up[2][2], left[2][2], left[1][2], left[0][2], down[2][0], down[2][1], down[2][2], right[0][0], right[1][0], right[2][0]
        elif square == 'B':
            for _ in range(turns):
                back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1], back[2][0], back[1][0] = back[2][0], back[1][0], back[0][0], back[0][1], back[0][2], back[1][2], back[2][2], back[2][1]
                up[0][0], up[0][1], up[0][2], right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], left[0][0] = right[0][2], right[1][2], right[2][2], down[0][0], down[0][1], down[0][2], left[2][0], left[1][0], left[0][0], up[0][0], up[0][1], up[0][2]
        elif square == 'L':
            for _ in range(turns):
                left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1], left[2][0], left[1][0] = left[2][0], left[1][0], left[0][0], left[0][1], left[0][2], left[1][2], left[2][2], left[2][1]
                front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], back[1][2], back[0][2], up[0][0], up[1][0], up[2][0] = up[0][0], up[1][0], up[2][0], front[0][0], front[1][0], front[2][0], down[2][2], down[1][2], down[0][2], back[2][2], back[1][2], back[0][2]
        elif square == 'R':
            for _ in range(turns):
                right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1], right[2][0], right[1][0] = right[2][0], right[1][0], right[0][0], right[0][1], right[0][2], right[1][2], right[2][2], right[2][1]
                up[0][2], up[1][2], up[2][2], front[0][2], front[1][2], front[2][2], down[2][0], down[1][0], down[0][0], back[2][0], back[1][0], back[0][0] = front[0][2], front[1][2], front[2][2], down[2][0], down[1][0], down[0][0], back[2][0], back[1][0], back[0][0], up[0][2], up[1][2], up[2][2]
        ### 디버깅
        # print('윗면')
        # for l in up:
        #     print(*l)
        # print('아랫면')
        # for l in down:
        #     print(*l)
        # print('앞면')
        # for l in fron:
        #     print(*l)
        # print('뒷면')
        # for l in back:
        #     print(*l)
        # print('좌')
        # for l in left:
        #     print(*l)
        # print('우')
        # for l in right:
        #     print(*l)
    ### 최종 출력
    for l in up:
        print(''.join(l))