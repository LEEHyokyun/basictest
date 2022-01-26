#N개의 자연수로 구성된 수열이 있을때
#합이 M인 부분적인 연속 수열의 개수를 구하는 알고리즘은?

##투포인터 알고리즘(시작점과 끝점을 지정하여 접근하는 데이터의 범위를 표현하는 것)
n = 5 #데이터 개수
m = 5 #연속수열의 부분합
data = [1, 2, 3, 2, 5]

count = 0
sum = 0
end = 0

for start in range(n):
    #start는 전체 반복문에서 반복, 이 경우는 합이 m보다 클 때
    #아래 경우는 end를 +1한 경우로 합이 m보다 작을때
    while sum < m and end < n: #추가조건 : end가 n보다 작을때만
        sum = sum + data[end] #일전의 합이 sum에 저장
        end = end + 1
    if sum == m: #부분합이 m일때 카운트 증가
        count = count + 1
    #이후 수행되는 알고리즘은 sum이 크거나 같다면 start + 1
    #이전 start 값에 대한 값은 감산
    sum = sum - data[start]

print(count)
