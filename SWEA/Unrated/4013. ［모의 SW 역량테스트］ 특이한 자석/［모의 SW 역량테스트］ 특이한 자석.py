### 입력 받기
T = int(input())
for tc in range(1, T+1):
    K = int(input())
    lst = [[]]+[[x for x in list(input()) if x in ['0','1']] for _ in range(4)] ### 톱니바퀴 형태
    for _ in range(K):
        num, dir = map(int, input().split())
        dirlst = [0]*5 ### 추후 톱니바퀴 회전 체크 리스트
        dirlst[num] = dir
        nearlst = [(lst[1][2]==lst[2][-2]), (lst[2][2]==lst[3][-2]), (lst[3][2]==lst[4][-2])]

        ### 부여 번호에 따른 각 바퀴 회전 알아보기
        if num == 1: ### 1번 톱니라면 순서대로 체크해야함
            idx = 2
            for i in range(3):
                if not nearlst[i]: ### 1번과 2번이 다르다면
                   dirlst[idx] = dirlst[idx-1]*(-1)
                   idx += 1
                else: break

        elif num == 2: ### 2번 톱니라면
            if not nearlst[0]:
                dirlst[1] = dir*(-1)
            idx = 3
            for i in range(1,3):
                if not nearlst[i]: ### 다르다면
                   dirlst[idx] = dirlst[idx-1]*(-1)
                   idx += 1
                else: break

        elif num == 3:
            if not nearlst[2]:
                dirlst[4] = dir*(-1)
            idx = num
            for i in range(1,-1,-1):
                if not nearlst[i]: ### 1번과 2번이 다르다면
                   dirlst[idx-1] = dirlst[idx]*(-1)
                   idx -= 1
                else: break

        else:
            idx = num
            for i in range(2, -1, -1):
                if not nearlst[i]:  ### 1번과 2번이 다르다면
                    dirlst[idx - 1] = dirlst[idx] * (-1)
                    idx -= 1
                else: break

        ### 회전시키기
        for k in range(1,5):
            if dirlst[k] == 0: continue
            elif dirlst[k] == 1: lst[k] = [lst[k][-1]] + lst[k][:-1]### 시계 방향
            else: lst[k] = lst[k][1:] + [lst[k][0]]
    ### 최종 점수 계산
    answer = 0
    if lst[1][0] == '1': answer += 1
    if lst[2][0] == '1': answer += 2
    if lst[3][0] == '1': answer += 4
    if lst[4][0] == '1': answer += 8
    print(f"#{tc} {answer}")
