N = int(input())

s = []

for _ in range(N):
    num = int(input())
    if num == 0:
        s.pop()
    else:
        s.append(num)

print(sum(s))
