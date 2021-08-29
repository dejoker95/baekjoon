N, K = map(int, input().split())
base = 1000000007

"""
n! / (n-k)! * k!
"""


def power(num, exp, base):
    if exp == 1:
        return num
    else:
        temp = power(num, exp // 2, base)
        if exp % 2 == 0:
            return temp * temp % base
        else:
            return temp * temp * num % base


l = [0 for i in range(4000001)]
l[0] = 1
l[1] = 1
# n!
for i in range(2, N + 1):
    l[i] = l[i - 1] * i
    if l[i] >= base:
        l[i] %= base

numerator = l[N]
denominator = (l[N - K] * l[K]) % base
result = (numerator % base) * (power(denominator, base - 2, base) % base) % base
print(result)

p = 7
a = 13