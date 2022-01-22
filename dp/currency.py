#N가지 종류의 화폐가 있다.
#화폐의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 구성하고자 한다.
#M원을 만들기 위한 최소 화폐의 개수는?

#첫째줄에 N, M이 주어진다
#N개의 줄에는 화폐의 가치가 주어진다.

#"적절한", "여러가지 종류"를 이용하여 최적의 해를 구하는 방법
#전형적인 DP, bottom up

##ai는 금액 a원을 만드는데 필요한 최소한의 화폐 개수(최적의 해)
##DP연산에서 나오는 최적의 해처럼
##INF = 10001

import sys
n, m = map(int, sys.stdin.readline().split())
#n줄의 화폐 정보를 입력받을때
currency = [int(sys.stdin.readline().strip()) for i in range(n)]

d = [10001] * (m+1)
d[0] = 0

#n개의 화폐 정보
for i in range(n):
    #화폐금액
    for j in range(currency[i], m+1):
        #최소 화폐단위부터 m원까지 가능한 경우의 수를
        #bottom up으로 계산한다.
        print(j)
        if d[j-currency[i]] != 10001:
            d[j] = min(d[j], d[j-currency[i]]+1)


if d[m] == 10001:
    print -1
else:
    print(d[m])