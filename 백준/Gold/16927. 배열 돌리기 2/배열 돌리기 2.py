### 1차 시도 : 124496kb 196ms
### 진짜 단순 무식하게 직접 구현했다.
### 아이디어 방식은 외곽 줄의 값들을 리스트로 만들어서 R번 회전시킨 다음에 다시 넣는 방식 사용
### R의 크기가 너무 컸지만 리스트 길이의 나머지 연산을 통해 단축
### 2차 시도 :
### 겹치는 부분을 합칠 수 있다고 판단 즉, 함수 2개를 합침
### 합치는 과정에서 범위 및 인덱싱하는거 계산이 헷갈림
import sys
input = sys.stdin.readline

### 입력 받기
N, M, R = map(int,input().rstrip().split())
arr = [input().rstrip().split() for _ in range(N)]

### R번 회전시키는 함수
def turns():
    for x in range(min(N//2, M//2)):
        line = [arr[x][i] for i in range(x, M-x)]
        line += [arr[i][M-1-x] for i in range(x+1, N-1-x)]
        line += [arr[N-1-x][i] for i in range(x, M-x)][::-1]
        line += [arr[i][x] for i in range(x+1, N-1-x)][::-1]

        length = len(line)
        newline = line[R%length:] + line[:R%length]

        idx = 0
        for i in range(x, M-x):
            arr[x][i] = newline[idx]
            idx += 1
        for i in range(x+1, N-1-x):
            arr[i][M-1-x] = newline[idx]
            idx += 1
        for i in range(M-x-1, x-1, -1):
            arr[N-1-x][i] = newline[idx]
            idx += 1
        for i in range(N-1-1-x, x, -1):
            arr[i][x] = newline[idx]
            idx += 1
    return arr

for i in turns():
    print(*i)