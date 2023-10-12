import heapq
from collections import deque

T = int(input())
for tc in range(1, T+1):
    N, M, K, A, B = map(int, input().split())
    receptiontime = list(map(int, input().split()))
    repairtime = list(map(int, input().split()))
    visitedtime = list(map(int, input().split()))
    visitedtime = [(visitedtime[idx], idx+1) for idx in range(K)]
    heapq.heapify(visitedtime)
    receptionlst, repairlst = [[0]*2 for _ in range(N)], [[0]*2 for _ in range(M)]
    resultdict = {num: [0,0] for num in range(1, K+1)}
    waitlst = deque()
    ### 시작
    nowtime = 0
    remain = K
    while remain>0:
        ### 접수 창구 관리
        for ridx in range(N):
            if receptionlst[ridx] == [0,0]: ### 아무도 없는 경우
                if visitedtime:
                    newtime, newvisitor = heapq.heappop(visitedtime)
                    if newtime <= nowtime:
                        receptionlst[ridx] = [receptiontime[ridx]+nowtime, newvisitor]
                        resultdict[newvisitor][0] = ridx+1
                    else:
                        heapq.heappush(visitedtime, (newtime, newvisitor))
            else: ### 누가 있는 경우
                if receptionlst[ridx][0] > nowtime: continue
                else:
                    endvisitor = receptionlst[ridx][1] ### 끝난 사람
                    waitlst.append(endvisitor)
                    if visitedtime:
                        newtime, newvisitor = heapq.heappop(visitedtime)
                        if newtime <= nowtime:
                            receptionlst[ridx] = [receptiontime[ridx] + nowtime, newvisitor]
                            resultdict[newvisitor][0] = ridx+1
                        else:
                            heapq.heappush(visitedtime, (newtime, newvisitor))
                            receptionlst[ridx] = [0,0]
                    else: receptionlst[ridx] = [0,0]

        ### 정비 창구 관리
        for pidx in range(M):
            if repairlst[pidx] == [0,0]: ### 아무도 없는 경우
                if waitlst:
                    newcustomer = waitlst.popleft()
                    repairlst[pidx] = [repairtime[pidx]+nowtime, newcustomer]
                    resultdict[newcustomer][1] = pidx+1
            else: ### 누가 있는 경우
                if repairlst[pidx][0] > nowtime: continue
                else:
                    endvisitor = repairlst[pidx][1] ### 끝난 사람
                    remain -= 1
                    if waitlst:
                        newcustomer = waitlst.popleft()
                        repairlst[pidx] = [repairtime[pidx] + nowtime, newcustomer]
                        resultdict[newcustomer][1] = pidx+1
                    else: repairlst[pidx] = [0,0]

        ### 디버깅
        # print('현재 시간', nowtime)
        # print('접수 창구')
        # print(receptionlst)
        # print('중간 대기', waitlst)
        # print('정비 창구')
        # print(repairlst)
        # print()

        ### 시간 추가
        nowtime += 1
    answer, cnt = 0, 0
    for num in range(1, K+1):
        if resultdict[num] == [A,B]:
            answer += num
            cnt += 1
    if cnt == 0: answer = -1
    # print(resultdict)
    print(f"#{tc} {answer}")

