numbers = [30, 3, 34, 5, 9, 990, 99]


def change(n):
    n = list(str(n))
    n.insert(1, ".")
    n = "".join(n)
    return float(n)


numbers.sort(key=lambda x: (change(x), -len(str(x))), reverse=True)
print(numbers)