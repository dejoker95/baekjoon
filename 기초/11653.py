def isPrime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def makePrime(n):
    if isPrime(n) == True:
        print(n)
    else:
        for i in range(2, n):
            if n % i == 0:
                print(i)
                makePrime(int(n/i))
                break


n = int(input())
makePrime(n)
