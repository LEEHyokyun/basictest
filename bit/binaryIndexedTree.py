#데이터 업데이트가 가능한 상황에서의 구간합
#바이너리 인덱스 트리, BIT

#N(1<=N<=1000K)개의 수가 있고, 중간에 수의 변경이 번번히 일어난다.
#이 상황에서 어떤 부분수열의 합을 구하려고 한다.
#데이터 변경횟수를 M(1<=M<=10K), 구간합 계산 횟수를 K(1<=K<=10K)라 하자.
#이때 구간의 합을 구할 수 있는 알고리즘을 어떻게 구성할 수 있을까

import sys
#데이터 개수, 변경횟수, 구간 합 계산 횟수
n, m, k = map(int, sys.stdin.readline().split())

#전체 데이터와 인덱스 트리를 배열에 나타낸다.
#인덱스 1부터 연산하는 것에 유의
arr = [0] * (n+1)
tree = [0] * (n+1)

#i번째 수까지 누적 합을 계산하는 함수
def prefixSum(i):
    result = 0
    while i > 0:
        result = result + tree[i]
        #0이 아닌 마지막 비트만큼 빼가면서 이동
        i = i - (i&-i)
    return result

#i번째 수를 특정 값만큼 더할때(값 업데이트)
def update(i, dif):
    while i <= n:
        tree[i] = tree[i] + dif
        i = i + (i&-i)

#구간합
def intervalSum(start, end):
    return prefixSum(end) - prefixSum(start - 1)

#문제
for i in range(1, n + 1):
    x = int(sys.stdin.readline())
    arr[i] = x
    #부분 수열 업데이트
    update(i, x)

for i in range(m+k):
    a, b, c = map(int, sys.stdin.readline().split())
    # 업데이트 연산일 경우
    if a==1:
        update(b,c-arr[b]) #바뀐 크기를 적용
        arr[b] = c
    else: #구간합
        #b-left
        #c-right
        print(intervalSum(b,c))