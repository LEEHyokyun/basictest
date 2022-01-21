#특정 범위에 속하는 데이터의 개수 구하기
#범위 내 속하는 데이터 개수를 구하는 메소드는 별도 구현이 필요
#파이썬의 이진탐색 라이브러리인 bisect을 이용한다.

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

print(count_by_range(a, 4, 4))
print(count_by_range(a, 1, 2))