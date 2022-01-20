#두개의 배열 A, B가 있다.
#두 배열은 N개의 원소로 구성되어있고, 모두 자연수이다.
#이때 최대 K번의 바꿔치기를 할 수 있는데, 바꿔치기란 배열A,B의 원소를 서로 바꾸는 작업을 의미한다.
#최종적을 배열 A의 원소 합이 최대가 되도록 알고리즘을 구성하고자 할 때, 만들 수 있는 배열 A의 모든 원소값 합계의 최대값은?

#첫번째 줄에 N, K가 공백을 기준으로 입력된다.
#두번째 줄에 배열A, 세번째 줄에 배열B가 입력된다.

#이때 핵심 아이디어는, 매번 배열 A에서 가장 작은 원소를 고르고 배열 B의 최대 원소와 교체한다는 점이다.
#A는 오름차순 정렬, B는 내림차순 정렬
#A의 원소가 B보다 작을 경우에만 교체를 진행
#퀵정렬 사용
import sys
n, k = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break #바로 다음 반복문 실행

print(sum(a))