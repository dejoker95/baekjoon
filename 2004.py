n, m = map(int, input().split())


def count_two(n):
    count = 0
    while n != 0:
        n //= 2
        count += n
    return count


def count_five(n):
    count = 0
    while n != 0:
        n //= 5
        count += n
    return count


two = count_two(n) - count_two(m) - count_two(n - m)
five = count_five(n) - count_five(m) - count_five(n - m)

print(min(two, five))
