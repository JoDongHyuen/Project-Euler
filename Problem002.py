# --------------------------------------
# Even Fibonacci numbers
# --------------------------------------

DP = [1, 2]

sum = 2

while True:
    fibo = DP[-1] + DP[-2]
    
    if fibo > 4000000:
        break

    if fibo % 2 == 0:
        sum += fibo
    
    DP.append(fibo)

print(sum)