N = int(input())
num = list(map(int, input().split()))

increase = [0 for i in range(N)]
decrease = [0 for i in range(N)]

max_cnt = 0

for i in range(N):
    for j in range(i):
        if num[i] > num[j] and increase[i] < increase[j]:
            increase[i] = increase[j]
    increase[i] += 1

for i in range(N - 1, -1, -1):
    for j in range(N - 1, i, -1):
        if num[i] > num[j] and decrease[i] < decrease[j]:
            decrease[i] = decrease[j]
    decrease[i] += 1


for i in range(N):
    s = increase[i] + decrease[i]
    if max_cnt < s:
        max_cnt = s
print(max_cnt - 1)