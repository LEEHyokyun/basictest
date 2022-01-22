#개미전사는 부족한 식량을 조달받기 위해 일렬로 나열된 창고에 접근하고자 한다.
#나열된 창고에서 서로 인접한(연속된) 창고에서 조달하지 않고, 최소한 한 칸 이상 떨어진 창고들로부터 식량을 조달받고자 한다.
#위 조건을 만족하면서 개미전사가 얻을 수 있는 최대식량을 구하는 알고리즘은 무엇인가?

##첫번째 줄에는 식량창고의 수인 N, 두번째 줄에는 각 창고에 저장된 식량의 개수가 배열로 주어진다.

import sys
N = int(input())
array = list(map(int, sys.stdin.readline().split()))
d = [0] * 100
#bottomup
#dpTable 부터 bottom up 시작되고, 식량의 양이 아닌 최종 결과임을 기억.
#0은 최초값, 1은 0과 1중에 큰 값을 선택하면 된다.
d[0] = array[0]
d[1] = max(array[0], array[1])

#이전에 도출한 최적의 해는 이후에도 그대로 적용된다.
for i in range(2, N):
    d[i] = max(d[i-1], d[i-2] + array[i])
    #d[i] = max((d[i - 1] + array[i]),(d[i-2] + array[i]))
    print(d[i])

