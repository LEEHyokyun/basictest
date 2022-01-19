#문자열 재정렬
#알파벳대문자와 숫자로 구성된 문자열이 주어진다.
#이때 모든 알파벳을 오름차순으로 출력하고, 그 뒤에 모든 숫자의 합을 붙인 문자열을 출력한다.

INPUT = input()
#알파벳은 별도의 리스트에 저장
#숫자는 따로 합을 구해서 리스트에 append
result = []
value = 0

for string in INPUT:
    #이러한 메소드들을 잘 활용할 수 있어야 한다
    #아스키코드 이렇게 복잡하게 생각할 필요가 없음
    if string.isalpha():
        result.append(string)
    else:
        value = value + int(string)

#알파벳 오름차순 정렬
result.sort()
#숫자가 하나라도 존재한다면 뒤에 그대로 삽입
if value != 0:
    result.append(str(value))

#이상태는 리스트 형태
print(result)
#이를 문자열로 변환하여 출력
#리스트에 포함되어있는 문자열들을 join(쭉 나열)
#기준에 맞추어 나열('' -> 공백없이)
print(' '.join(result))


