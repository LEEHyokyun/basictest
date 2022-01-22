#정수 X가 주어졌을 떄 정수X에 사용할 수 있는 연산은 다음과 같이 4가지가 존재한다.
##X가 5로 나누어 떨어지면 5로 나눈다.
##X가 3으로 나누어 떨어지면 3으로 나눈다.
##X가 2로 나누어 떨어지면 2로 나눈다.
##X에서 1을 뺀다.
#위 연산 4가지를 적절히 활용하여 1을 만들고자 할 때, 연산을 사용하는 횟수의 최소값은?

#단순히 greedy(나누기 기준)를 적용할 수는 없다.
#2/3/5를 나누는 과정을 적절히 섞어서 적용해야 하는데, 점화식으로 설정할 수 있다.
#적절히 섞어서 사용하는 과정을 점화식으로 표현할 수 있다.
#f(N) = min(f(N//2)+f(N//3)+f(N//5)+f(N-1)) + 1
#단 f(N)은 N에 대한 optimal solution

X = int(input())

d = [0] * 30001

#0과 1에 대한 해는 연산 과정이 없으므로 0으로 설정
for i in range(2, X+1):
    #2,3,5로 나누어 떨어지는 경우
    #각 숫자를 나눈 경우, 특히 나누는 수가 여러개가 적용될 수 있는 경우
    #각 경우의 수마다 최적의 해(최소값)를 교체하는 조건식을 작성
    if i%2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i%3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
    if i%5 == 0:
        d[i] = min(d[i], d[i//5] + 1)
    #나누어 떨어지지 않는다면
    d[i] = d[i-1] + 1

print(d[X])





