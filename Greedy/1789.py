S = int(input())

s = 0
i = 1
while True:
    s += i
    if s == S:
        print(i)
        break
    if s > S:
        print(i - 1)
        break
    i += 1