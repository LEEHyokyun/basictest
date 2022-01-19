#정수 N이 입력되면
#00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중
#3이 하나라도 포함되어있는 모든 경우의 수를 구하는 알고리즘은?

#모든 경우의 수
#완전탐색(구현유형, Brute Forcing)

#python에서 수용하는 1초 연산횟수는 약 2천만법
#가능한 모든 경우의 수를 탐색하는 방법

H = int(input())
count = 0

#시 - 분 - 초
for i in range(H + 1):
    for j in range(60):
        for k in range(60):
            #시간, 분, 초에 대해 문자열을 만들고, 해당 문자가 포함되어있는지 아래와 같이 기술
            if str(H) in str(i)+str(j)+str(k):
                count = count + 1

print(count)