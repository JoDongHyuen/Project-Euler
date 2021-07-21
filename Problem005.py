# --------------------------------------
# Smallest multiple
# --------------------------------------
# 1 ~ 20 으로 나눠지는 수 중에 가장 작은 수 찾기

import math

result = 2

for i in range(3, 21):
    GCD = math.gcd(result, i)
    result = result // GCD * i

print(result)


# 개선안
# 16은 2^4, 32는 2^5임, 여기서 2~20 사이의 숫자는 2를 소인수로 최대 4개를 가질 수 있다는 것을 의미
# 이런 방식으로 2^4 * 3^2 * 5 * 7 * 11 * 13 * 17 * 19 를 하면 정답이 나옴

prime = []

num = [True for i in range(21)]

for i in range(2, 21):
    if num[i] == True:
        prime.append(i)

        mul = i
        while mul <= 20:
            num[mul] = False
            mul += i

limit = math.sqrt(20)

result = 1

for pri in prime:
    if pri < limit:
        exp = math.floor(math.log(20) / math.log(pri)) # 이 부분 생각 트이는데 아주 좋았음 (로그 밑변환 활용)
        result *= pri ** exp
    else:
        result *= pri

print(result)