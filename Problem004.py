# --------------------------------------
# Largest palindrome product
# --------------------------------------
# 세 자리수 두개를 곱해서 나오는 팰린드롬 수 중에 가장 큰 값 구하기


def isPalindrome(check):
    length = len(check) // 2

    for i in range(length):
        if check[i] != check[-1 - i]:
            return False 
    return True

Palindrome = []

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if isPalindrome(str(i * j)):
            Palindrome.append(i * j)

print(max(Palindrome))


# 개선안 1
# j는 점점 작아지는 상황에서 i * j 가 변수 result보다 작으면, 나중에 i * j가 대칭수일지라도 result 가 될 수 없음 그래서 바로 break를 함
# 그리고 result보다 작은 값은 걸러냈기 때문에 i * j 가 대칭수면 항상 result보다 클 수 밖에 없음

result = 0

for i in range(999, 99, -1):
    for j in range(i, 99, -1):
        if i * j <= result:
            break
        if isPalindrome(str(i * j)):
            result = i * j

print(result)


# 개선안 2
# 정답은 항상 6자리 수임, (세 자리수 두 개를 곱했기 때문에)

# P=100000x + 10000y + 1000z + 100z + 10y + x
# P=100001x + 10010y + 1100z
# P=11(9091x + 910y + 100z)

# 위와 같이 11을 소인수로 가진다고 하는데, 원래 짝수 대칭수는 11로 나눠진다고 함

A = 999
result = 0

while A >= 100:

    if A % 11 == 0:
        B = 999
        db = 1
    else:
        B = 990
        db = 11

    while B >= A :
        mul = A * B
        
        if mul >= result:
            check = isPalindrome(str(A * B))
            if check:
                result = mul
            
        B -= db

    A -= 1 

print(result)