def mergesort(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    left = mergesort(arr[:mid])
    right = mergesort(arr[mid:])

    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            merged.append(left[l])
            l += 1
        else:
            merged.append(right[r])
            r += 1
    merged += left[l:]
    merged += right[r:]
    return merged



n = int(input())
l = []
for i in range(n):
    l.append(int(input()))
result = mergesort(l)
for num in result:
    print(num)

