import math

def primeList(n):
    prime  = [True] * n
    for i in range(2, int(math.sqrt(n))+1):
        if prime[i] == True:
            for j in range(i*2, n, i):
                prime[j] = False
    return [i for i in range(2, n) if prime[i] == True]

def getPrime(n, prime):
    prime = primeList(n)
    idx = max([i for i in range(len(prime)) if prime[i] <= n/2])
    for i in range(idx, -1, -1):
        for j in range(i, len(prime)):
            if prime[i] + prime[j] == n:
                return prime[i], prime[j]

case = int(input())

for i in range(case):
    n = int(input())
    result = getPrime(n)  
    print("{} {}".format(result[0], result[1]))


