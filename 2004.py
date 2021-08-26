n, m = map(int, input().split())


def count_five(n):
    count = 0
    for i in range(1, n + 1):
        if i % 5 == 0:
            num = i
            while True:
                count += 1
                num /= 5
                if num % 5 != 0:
                    break
    return count


ans = 0
if m == 0:
    ans = 0
elif n == 1:
    ans = 0
else:
    ans = count_five(n) - (count_five(m) + count_five(n - m))

print(ans)
