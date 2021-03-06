#N명의 병사가 무작위로 나열되어 있다.
#병사를 배치할 때는 전투력이 내림차순으로 배치하고자 한다.
#무작위로 나열되어있는 상태에서 병사들을 열외시켜 내림차순 배열을 구현하고자 할때, 병사수가 최대로 남게하는 방안은?

#첫째줄에 N(병사수)이 주어지고, 둘째줄에 공백을 기준으로 전투력이 나열된다.
#첫째줄에 남아있는 병사수가 최대로 남아있도록 열외시켜야하는 병사의 수

#오름차순에서 부분적으로 감소하는 수열을 제거하는 LIS 알고리즘을 적용하는 전형
#D[i]는 array[i]를 마지막 원소를 가지는 부분수열의 최대 길이라 할 때
#점화식은 D[i] = max(D[i], D[j]+1) (단, j<i이고 array[j] < array[i])
#D[j]까지의 최적의 해에 i가 추가되면 길이가 1이 늘어나므로 +1을 한 것.
#기존의 LIS는 오름차순정렬이고, 본 문제에서는 이를 내림차순으로 적용하면 된다.

import sys
N = int(input())
array = list(map(int, sys.stdin.readline().split()))
array.reverse()

dp = [1]*N

#DP를 적용하여 LIS구현
for i in range(1, N):
    #이중반복으로 비교대상 순회
    for j in range(0, i):
        #오름차순 정렬을 만족하였을때 점화식 적용
        #비교대상 array[j]는 항상 순회하고 바뀌다는 것에 유의
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j]+1) #dp[i]는 최적의 해를 구하는 과정으로 순회하면서 바뀔 수 있음

#열외해야하는 병사의 최소 수
print(N-max(dp))