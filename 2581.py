def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

m = int(input())
n = int(input())

l = []
for i in range(m, n+1):
    if isPrime(i) == True:
        l.append(i)

if len(l) == 0:
    print(-1)
else:
    print(sum(l))
    print(min(l))
