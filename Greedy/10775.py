import sys


def find(num):
    if num == parent[num]:
        return num
    parent[num] = find(parent[num])
    return parent[num]


def union(x, y):
    x = find(x)
    y = find(y)
    parent[x] = y


G = int(sys.stdin.readline())
P = int(sys.stdin.readline())
planes = [int(sys.stdin.readline()) for _ in range(P)]

parent = [i for i in range(G + 1)]


count = 0
for plane in planes:
    x = find(plane)
    if x == 0:
        break
    union(x, x - 1)
    count += 1
print(parent)
print(count)