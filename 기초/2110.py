import sys

N, C = map(int, sys.stdin.readline().split())

house = [int(sys.stdin.readline()) for i in range(N)]

house.sort()

start = 1
end = house[-1] - house[0]

result = 0
while start <= end:
    mid = (start + end) // 2
    count = 1
    first_house = house[0]

    for i in range(1, len(house)):
        if house[i] >= first_house + mid:
            count += 1
            first_house = house[i]

    if count >= C:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
print(result)