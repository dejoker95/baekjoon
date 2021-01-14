import sys

case = int(sys.stdin.readline())
temp = []
for i in range(case):
    info = sys.stdin.readline().split()
    age = int(info[0])
    name = info[1]
    order = i
    t = (age, name, order)
    temp.append(t)

def merge(temp):
    if len(temp) < 2:
        return temp
    mid = len(temp)//2
    left = merge(temp[:mid])
    right = merge(temp[mid:])

    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l][0] < right[r][0]:
            merged.append(left[l])
            l += 1
        elif left[l][0] == right[r][0]:
            if left[l][2] < right[r][2]:
                merged.append(left[l])
                l += 1
            else:
                merged.append(right[r])
                r += 1
        else:
            merged.append(right[r])
            r += 1
    merged += left[l:]
    merged += right[r:]
    return merged

temp = merge(temp)
for i in temp:
    print(i[0], i[1])
