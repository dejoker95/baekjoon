import sys

N = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(N)]

alphabet = [0] * 26

for word in words:
    i = 0
    while word:
        cur = word[-1]
        alphabet[ord(cur) - ord("A")] += 10 ** i
        i += 1
        word = word[:-1]

alphabet.sort(reverse=True)
ans = 0
for i in range(9, 0, -1):
    ans += i * alphabet[9 - i]

print(ans)
