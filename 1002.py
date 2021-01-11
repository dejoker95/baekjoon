import math

def get(x1, y1, r1, x2, y2, r2):
    dist = math.sqrt((x1-x2)**2 + (y1-y2)**2)
    if x1 == x2 and y1 == y2 and r1 == r2:
        return -1
    if x1 == x2 and y1 == y2 and r1 != r2:
        return 0
    if dist > r1 + r2:
        return 0
    if dist == r1 + r2:
        return 1
    if dist < r1 + r2:
        if (r1 == dist + r2) or (r2 == dist + r1):
            return 1
        elif (r1 > dist + r2) or (r2 > dist + r1):
            return 0
        else:
            return 2

n = int(input())
for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    print(get(x1, y1, r1, x2, y2, r2))
