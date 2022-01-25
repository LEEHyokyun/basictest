#소수 판별하기
import math

def isPrimeNumber(x):
  for i in range(2, int(math.sqrt(x))+1):
    if x % i == 0:
      return False
    else:
      return True

print(isPrimeNumber(5))