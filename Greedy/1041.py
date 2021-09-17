import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))


def count(n):
    one = (n - 2) ** 2 + (n - 2) * (n - 1) * 4
    two = 4 * (n - 2) + 4 * (n - 1)
    three = 4
    return one, two, three


if N == 1:
    print(sum(nums) - max(nums))
else:
    sumList = []
    sumList.append(min(nums[0], nums[5]))
    sumList.append(min(nums[1], nums[4]))
    sumList.append(min(nums[2], nums[3]))
    sumList.sort()

    one, two, three = count(N)
    print(one * sumList[0] + two * sum(sumList[:2]) + three * sum(sumList))
