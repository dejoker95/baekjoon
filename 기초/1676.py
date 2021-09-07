n = int(input())

if n == 0:
    print(0)
else:
    count = 0
    for i in range(1, n + 1):
        if i % 5 == 0:
            num = i
            while True:
                count += 1
                num /= 5
                if num % 5 != 0:
                    break
    print(count)