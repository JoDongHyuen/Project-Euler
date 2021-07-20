# --------------------------------------
# Largest prime factor
# --------------------------------------

from timeit import timeit
import math


num = 600851475143

result = []
div = 2

while num != 1:
    if num % div == 0:
        result.append(div)
        num //= div
    else:
        div += 1

print(result[-1])

# 개선안 1
# 2를 제외한 모든 소수는 홀수임
# So 2로 나눠질 때까지 최대한 나눈뒤 div를 2씩 증가

num = 600851475143

result = []
while True:
    if num % 2 == 0:
        num //= 2
        result.append(2)
    else:
        break

div = 3
while num != 1:
    if num % div == 0:
        result.append(div)
        num //= div
    else:
        div += 2

print(result[-1])


# 개선안 2
# 위 방식에서 div가 처음 num의 루트 값보다 커졌을 때,
# 연산을 통해 나눠진 num의 값이 처음 num의 루트 값보다 크다면 그 값은 무조건 소수임

# 예를 들어 num이 14인 경우 루트 14은 3.xxxx
# 14는 2로 나눠져서 num은 7로 업데이트 됨
# div는 3,5,7 이렇게 증가해야하지만 5는 루트14 보다 크기 때문에 반복문은 끝나고 num은 소수가 됨

num = 600851475143
root = int(math.sqrt(num)) + 1

result = []
while True:
    if num % 2 == 0:
        num //= 2
        result.append(2)
    else:
        break

div = 3
while num != 1:
    if num % div == 0:
        result.append(div)
        num //= div
    else:
        if div > root:
            break
        div += 2

if num > root:
    print(num)
else:
    print(result[-1])
    