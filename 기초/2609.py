a, b = map(int, input().split())

small = min(a, b)

factor = 0
for i in range(small, 0, -1):
    if a % i == 0 and b % i == 0:
        factor = i
        break

print(factor)
print(a * b // factor)
