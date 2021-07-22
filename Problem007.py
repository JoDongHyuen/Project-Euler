# --------------------------------------
# 10001st prime
# --------------------------------------
# 10001 번째 소수 구하기


# 이 풀이는 임의의 입력에 대응할 수 없다
import math

num = 1000000
prime = []
check = [True] * (num + 1)
limit = int(math.sqrt(num))

for i in range(2, limit + 1):
    if check[i] == True:
        mul = i * 2
        while mul <= num:
            check[mul] = False
            mul += i

for i in range(2, num + 1):
    if check[i] == True:
        prime.append(i)

print(prime[10000])


# 개선안
# 3보다 큰 소수는 6의 배수에 1을 더하거나 1을 뺀 형태라고 함 (처음 안 사실..!)

def isPrime(n):
    if n == 1:
        return False
    elif n < 4:
        return True
    elif n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False
    else:
        r = math.floor(math.sqrt(n))
        f = 5
        while f <= r:
            if n % f == 0 : return False
            if n % (f + 2) == 0 : return False
            f += 6
        return True

target = 10001
count = 1 # 2는 카운트 된 걸로 체크
i = 1

while count != target:
    i += 2
    if isPrime(i):
        count += 1

print(i)