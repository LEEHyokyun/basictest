def binarySearch(array, target, start, end):
    if start > end: #탐색하고자하는 값이 탐색범위에 존재하지않는 경우
        return None
    mid = (start + end)//2

    if array[mid] == target:
        return mid #탐색완료
    elif array[mid] > target:
        return binarySearch(array, target, start, mid-1)
    else:
        return binarySearch(array, target, mid+1, end)

import sys
n, target = map(int, sys.stdin.readline().split()) #원소개수, 탐색대상
array = list(map(int, sys.stdin.readline().split())) #list

result = binarySearch(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)
