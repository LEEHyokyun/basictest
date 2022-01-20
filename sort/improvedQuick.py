array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick_sort(array):
    print(array)
    if len(array) <= 1:
        # left_side에서 첫번째 원소가 0일 경우, array가 empty될 수 있음
        # 따라서 탈출조건은 empty경우를 고려하여 =< 1이 되는 것이 좋음
        return array

    pivot = array[0]  # pivot값
    tail = array[1:]  # pivot을 제외한 리스트

    left_side = [x for x in tail if x <= pivot]
    # 데이터묶음을 pivot보다 작은 값들로
    right_side = [x for x in tail if x > pivot]
    # 데이터묶음을 pivot보다 큰 값들로

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


print(quick_sort(array))