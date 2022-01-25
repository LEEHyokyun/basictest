import math

# 1000까지의 소수 판별
n = 1000
array = [True for i in range(n+1)]

for i in range(2, int(math.sqrt(n))+1):
    #어떤 수의 배수들을 제거할지 판단하는 기준은
    #최초의 소수를 제외하고, 그 소수의 모든 배수를 제거한다.
    if array[i] == True:
        j = 2
        while i * j < n:
            #소수가 아닌 수들은
            #n의 제곱근 안에 속하는 약수들에 대하여
            #그 배수들이 제거되므로
            #곱하는 수 자체는(i)는 제곱근 내부의 수
            #단 제거할 때는 모든 범위에 대해서 제거
            array[i*j] = False
            j = j + 1

#모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')
