import sys

l = [0 for i in range(10001)]
n = int(sys.stdin.readline())

for i in range(n):
    idx = int(sys.stdin.readline())
    l[idx] += 1

for i in range(10001):
    if l[i] > 0:
        for j in range(l[i]):
            print(i)