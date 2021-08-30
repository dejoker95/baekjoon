import sys
from collections import Counter

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))

a = Counter(A)

ans = []
for t in T:
    ans.append(a[t])

print(*ans)
