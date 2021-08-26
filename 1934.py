N = int(input())
for i in range(N):
    a, b = map(int, input().split())

    if a == 1 or b == 1:
        print(a * b)
    elif max(a, b) % min(a, b) == 0:
        print(max(a, b))
    else:
        small = min(a, b)

        factor = 0
        for i in range(small // 2, 0, -1):
            if a % i == 0 and b % i == 0:
                factor = i
                break
        print(a * b // factor)