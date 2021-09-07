N = int(input())
time = []

for i in range(N):
    time.append(list(map(int, input().split())))


time = sorted(time, key=lambda x: (x[1], x[0]))


last = 0
count = 0

for start, end in time:
    if last <= start:
        last = end
        count += 1

print(count)
