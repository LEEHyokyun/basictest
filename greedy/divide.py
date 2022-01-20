#어떤 수 N이 1이 될 때까지 두 과정 중 하나는 반복수행한다.
##N에서 1을 뺀다
##N을 K로 나눈다
#단 두번째 연산은 N이 K로 나누어떨어질때 선택이 가능하다.
#이 과정을 최소로 수행하는 알고리즘은?

#K로 나눈 과정을 최대한 많이 수행하는 기준이 명확히 정해져있다.
#N은 항상 1에 도달할 수 있다
#그리디 알고리즘 적용 가능

import sys
N, K = map(int, sys.stdin.readline().split())

result = 0

while True:
    #N이 K로 나누어 떨어지는 수가 될 때까지 감안
    target = N // K * K #★이런 부분) N이 K로 나누어 떨어지지 않을 경우, 나누어 떨어지는 가장 가까운 수를 구하는 과정
    #그만큼 1을 뺌
    #최초값을 입력받은 경우에 해당
    result = result + N - target
    N = target

    #N이 K보다 작아 나누어떨어지지 않을 경우엔 반복문 탈출
    if N < K:
        break

    result = result + 1
    N = N // K

#남은건 뺴는 과정
result = result + (N-1)

print(result)




