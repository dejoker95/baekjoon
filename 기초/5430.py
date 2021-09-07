import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())
    nums = sys.stdin.readline()[1:-2]
    if nums == "":
        nums = []
    else:
        nums = deque(list(map(int, nums.split(","))))

    flag = "left"

    for c in p:
        if c == "R":
            if flag == "left":
                flag = "right"
            else:
                flag = "left"
        elif c == "D":
            if len(nums) == 0:
                flag = "error"
                break
            if flag == "left":
                nums.popleft()
            else:
                nums.pop()

    string = "["

    if flag == "error":
        print("error")
    elif len(nums) == 0:
        print("[]")
    elif flag == "left":
        for i in range(len(nums)):
            if i == len(nums) - 1:
                string += str(nums[i]) + "]"
            else:
                string += str(nums[i]) + ","
        print(string)
    else:
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                string += str(nums[i]) + "]"
            else:
                string += str(nums[i]) + ","
        print(string)