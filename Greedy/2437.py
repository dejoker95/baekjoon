import sys

N = int(sys.stdin.readline())
num = list(map(int, sys.stdin.readline().split()))

num.sort()


ans = 1
for i in range(N):
    if ans < num[i]:
        break
    ans += num[i]
print(ans)
