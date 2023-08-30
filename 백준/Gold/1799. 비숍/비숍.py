import sys
input = sys.stdin.readline
N = int(input().rstrip())
### 우하로 가는 방향의 대각선 그래프 생성
v1, v2 = {}, {}
maximumv1 = 2*(N-1)
maximumv2 = N-1
vlst1 = [0]*2*N
vlst2 = [0]*2*N
### v1 딕셔너리 채우기
vidx = 0
while vidx <= maximumv1:
    v1[vidx] = []
    vidx += 1
### v2 딕셔너리 채우기
vidx2 = -N
while vidx2 <=maximumv2:
    v2[vidx2] = []
    vidx2 += 1
### 딕셔너리 및 리스트 채우기
for i in range(N):
    linelst = input().rstrip().split()
    j = 0
    while j < N:
        if linelst[j] == '1':
            v1[i+j].append(i-j)
            v2[i-j].append(i+j)
        j += 1
# print(v1.items())
### 우하대각선 확인
answerv1 = 0
def bishop1(n, k):
    global answerv1
    if answerv1 == 2*N-2:
        return
    if maximumv1-n+k<=answerv1:
        return
    if n == maximumv1:
        answerv1 = max(answerv1,k)
        return
    if len(v1[n])>0:
        for num in v1[n]:
            if vlst2[num] == 0:
                vlst2[num] = 1
                bishop1(n+1,k+1)
                vlst2[num] = 0
    bishop1(n+1,k)
bishop1(0,0)
def bishop2(n, k):
    global answerv1
    if answerv1 == 2*N-2:
        return
    if maximumv2-n+k<=answerv1:
        return
    if n == maximumv2:
        answerv1 = max(answerv1,k)
        return
    if len(v2[n])>0:
        for num in v2[n]:
            if vlst1[num] == 0:
                vlst1[num] = 1
                bishop2(n+1,k+1)
                vlst1[num] = 0
    bishop2(n+1,k)
bishop2(-N,0)
print(answerv1)