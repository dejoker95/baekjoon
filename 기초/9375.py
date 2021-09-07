from collections import Counter

N = int(input())

for i in range(N):
    n = int(input())
    s = []
    for _ in range(n):
        name, category = input().split()
        s.append(category)
    ans = 1
    result = Counter(s)
    for key, val in result.items():
        ans *= val + 1
    print(ans - 1)