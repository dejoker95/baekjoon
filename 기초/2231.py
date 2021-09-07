def getSum(n):
    if n < 10:
        return n
    return n % 10 + getSum(n//10)

n = int(input())

for i in range(n):
    temp = i + getSum(i)
    if temp == n:
        print(i)
        break
    if i == n-1:
        print(0)

