#떡볶이 떡 만들기

#떡볶이 떡을 자르려고 하는데, 떡볶이 떡의 길이가 일정하지 않다.
#이 떡들은 절단기로 자르는데, 높이 H를 지정하면 길이가 H보다 큰 떡들을 한 번에 절단한다.
#손님이 가져가는 길이는 절단된 후의 떡들을가져간다.
#손님이 요청한 총 길이가 M일때 적어도 M만큼의 떡을 얻기 위해 절단기로 설정할 수 있는 높이의 최대값을 구해보자.

#첫째줄에 떡의 개수 N과 요청한 떡의 총 길이 M이 주어진다(공백기준).
#둘째줄에는 떡들의 개별 높이가 주어지고, 이 높이의 총합은 항상 M보다 크다.

##핵심은 조건에 맞는 최대 높이, 즉 파라메트릭 서치를 활용하는 문제이다.
##따라서 적절한 높이를 찾을때까지 이진탐색 및 판별 등을 수행하는데
##높이를 구한 후, 해당 높이를 통해 조건을 만족할 수 있는가를 판별한다.
##이 과정을 반복하면서 탐색범위를 좁혀나간다.
##Tip, 조건범위가 10억 등..큰 탐색범위를 본다면 이진탐색을 먼저 생각하는 것이 좋다.
import sys
n, m = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

#이진탐색 start node, end node
start = 0
end = max(array)

result = 0
while start <= end:
    total = 0 #순회할때마다 result 값은 일단 0을 저장한 것부터 시작
    mid = (start + end)//2
    print('mid value is', mid)
    for beforeHeight in array:
        if beforeHeight > mid:
            total = total + beforeHeight - mid
            print('total length is', total)
        #잔여길이 구하고 판별
    if total < m:
        end = mid-1
    else:
        result = mid
        start = mid+1

print(result)


