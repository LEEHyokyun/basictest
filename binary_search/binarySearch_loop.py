def binarySearch(array, target, start, end):

    while start <= end:
        mid = (start + end)//2

        if array[mid] == target:
            return mid #탐색완료
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    #위 반복문을 수행한후 탐색대상이 없어 탈출하였을 경우
    return None

import sys
n, target = map(int, sys.stdin.readline().split()) #원소개수, 탐색대상
array = list(map(int, sys.stdin.readline().split())) #list

result = binarySearch(array, target, 0, n-1)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result+1)
