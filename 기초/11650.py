import sys

case = int(sys.stdin.readline())
n = []
for i in range(case):
    x, y = map(int, sys.stdin.readline().split(' '))
    n.append((x, y))

def merge(n):
    if len(n) < 2:
        return n
    
    mid = len(n)//2
    left = merge(n[:mid])
    right = merge(n[mid:])

    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l][0] < right[r][0]:
            merged.append(left[l])
            l += 1
        elif (left[l][0] == right[r][0]) and (left[l][1] < right[r][1]):
            merged.append(left[l])
            l += 1
        elif (left[l][0] == right[r][0]) and (left[l][1] > right[r][1]):
            merged.append(right[r])
            r += 1
        else:
            merged.append(right[r])
            r += 1
    merged += left[l:]
    merged += right[r:]
    return merged

n = merge(n)
for t in n:
    print(t[0], t[1])