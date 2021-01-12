def hanoi(n, start, dest, other):
    if n < 2:
        print(start, dest)
        return
    hanoi(n-1, start, other, dest)
    print(start, dest)
    hanoi(n-1, other, dest, start)

n = int(input())
print((2**n)-1)
hanoi(n, 1, 3, 2)