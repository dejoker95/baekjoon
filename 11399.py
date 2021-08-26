N = int(input())
time = list(map(int, input().split()))

time = sorted(time)
result = 0
for i in range(N):
    result += sum(time[0 : i + 1])

print(result)