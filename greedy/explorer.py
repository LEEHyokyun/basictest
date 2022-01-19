#마을에 모험가 N명이 있다고 가정해보자.
#모험가 길드에서는 N명의 모험가를 대상으로 공포도를 측정하는데
#공포도가 X인 모험가는 반드시 X명 이상으로 구성해야 모험에 참가가능
#N명에 대한 모험가 정보가 주어졌을때 모험을 할 수 있는 그룹의 최대 수를 구하는 알고리즘은?

#핵심 : 일단 가장 낮은 수를 찾는다는 점에서 그리디 알고리즘이다.
#다만 별도의 기준으로, "오름차순 정렬" 후에 낮은 숫자부터 순차적으로 확인하여
#현재 그룹에 포함된 모험가의 수가 공포도 이상이라면 결과도출
import sys
# key point input() 및 이를 정수화
N = int(input())
# key point 입력받고 이를 바로 list화
data = list(map(int, sys.stdin.readline().split()))
data.sort()

#결과(그룹의 수)
result = 0
#현재 모험가의 수
count = 0

#이미 정렬되어있으므로 공포도를 낮은 것 부터 차례대로 확인
for i in range(len(data)):
    count = count + 1
    if count >= data[i]:
        result = result + 1
        #이 이후부터 다시 순회를 계속해야 하므로 count = 0
        count = 0

print(result)