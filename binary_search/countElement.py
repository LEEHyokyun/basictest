#N개의 원소를 포함하는 수열이 오름차순으로 정렬되어있다.
#수열에서 x가 등장하는 횟수를 고르는 알고리즘은(단, log(N)의 시간복잡도가 되도록 구현할 것)?
#x가 존재하지 않는다면 -1을 출력

#선형탐색으로는 무조건 시간초과
#이진탐색을 수행해야 원하는 결과를 얻을 수 있다

#정렬이 이미 수행된 상황이므로 이를 이용
#특정 값이 등장하는 첫번째 위치, 마지막 위치를 찾아 차이 계산(bisect)

from bisect import bisect_left, bisect_right

def count(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)

    return right_index-left_index

import sys
n, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

#값이 x~x 범위에 있는 데이터 개수 계산
result = count(array, x, x)
if result == 0:
    print -1
else:
    print(result)