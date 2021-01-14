import sys

case = int(sys.stdin.readline())
words = []
for _ in range(case):
    words.append(sys.stdin.readline().strip())
words = list(set(words))

def merge(w):
    if len(w) < 2:
        return w
    mid = len(w)//2
    left = merge(w[:mid])
    right = merge(w[mid:])

    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if len(left[l]) < len(right[r]):
            merged.append(left[l])
            l += 1
        elif len(left[l]) == len(right[r]):
            if left[l] < right[r]:
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

words = merge(words)
for word in words:
    print(word)
