N = input()

cnt = 1
base = N[0]
for i in range(1, len(N)):
    if N[i] != base:
        cnt += 1
        base = N[i]
print(cnt // 2)
