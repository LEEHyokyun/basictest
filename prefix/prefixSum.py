#접두사 합을 통한 구간 합 구하는 알고리즘 도출하기
n = 5
data = [10, 20, 30, 40, 50]

#sum result
sum = 0
#prefix sum, index = 0은 0으로 초기화, 노드1부터 계산하는 것임.
prefixSum = [0]

for i in data:
    sum = sum + i
    prefixSum.append(sum)

#구간합 계산
left = 3
right = 4
print(prefixSum[right]-prefixSum[left-1])
