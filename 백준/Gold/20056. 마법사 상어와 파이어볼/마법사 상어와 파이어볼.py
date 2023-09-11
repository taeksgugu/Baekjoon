### 1차 실패 원인 -> 모두 홀수거나 짝수인 경우 일반화를 잘못함
import sys
input = sys.stdin.readline
### 입력값 받기
N, M, K = map(int,input().rstrip().split())
arrdic = {}
for _ in range(M):
    ri, ci, mi, si, di = map(int, input().rstrip().split())
    arrdic[(ri-1,ci-1)] = [(mi,si,di)]

### 이동방향리스트 생성
dirlst = [(-1,0), (-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1)]

def solve():
    global arrdic
    time = 0
    while time < K:
        time += 1
        newdic = {}
        for i, j in arrdic.keys():
            lst = arrdic[(i,j)]
            for m, s, d in lst:
                di, dj = dirlst[d] ### 방향 좌표 가져오기
                ni, nj = (i+di*s)%N, (j+dj*s)%N ### 1행과 N행이 연결, 1열과 N열이 연결되어있기 때문에 해당 방식으로 좌표 처리
                if (ni,nj) in newdic:
                    newdic[(ni,nj)].append((m,s,d))
                else:
                    newdic[(ni,nj)] = [(m,s,d)]
        ### 같은 칸 2개 이상일 때
        ballcnt = 0 ### 남은 파이어볼 갯수 파악 -> 만약 0개가 된다면 while문을 break해도 됨
        for i, j in newdic.keys():
            lst = newdic[(i,j)]
            cnt = len(lst)
            if cnt >= 2:
                m_sum, s_sum, d_sum, even, odd = 0, 0, 0, 0, 0
                for m, s, d in lst:
                    m_sum += m
                    s_sum += s
                    d_sum += d
                    if d%2==0: even+=1
                    else: odd+=1
                if m_sum // 5 == 0:
                    newdic[(i,j)] = []
                else:
                    if even == 0 or odd == 0: ### 모두 홀수거나 짝수일 경우
                        newdic[(i,j)] = [(m_sum//5, s_sum//cnt, 0), (m_sum//5, s_sum//cnt, 2), (m_sum//5, s_sum//cnt, 4), (m_sum//5, s_sum//cnt, 6)]
                    else:
                        newdic[(i,j)] = [(m_sum//5, s_sum//cnt, 1), (m_sum//5, s_sum//cnt, 3), (m_sum//5, s_sum//cnt, 5), (m_sum//5, s_sum//cnt, 7)]
                    ballcnt += 4
            else:
                ballcnt += cnt
        if ballcnt == 0: ### 이미 0개일 경우 더 이상 해도 의미가 없기 때문에 바로 return
            return 0
        arrdic = newdic
    answer = 0
    for balls in arrdic.values():
        for m,s,d in balls:
            answer += m
    return answer
print(solve())
### 해당 코드 포인트 : 2차원 리스트를 생성해서 파이어볼의 위치를 기록하지 않고 딕셔너리로 좌표 추적
###                 입력 받을 때 바로 계산하기 편하게 -1 해서 좌표 입력받음
###                 합을 구하는 경우, map(sum, lst)를 고려했으나, 홀수 짝수 처리를 따로 해야해서 그냥 for문 사용