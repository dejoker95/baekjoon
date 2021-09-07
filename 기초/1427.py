import sys

num = list(sys.stdin.readline())
num.sort(reverse=True)
result = "".join(num)
print(result)