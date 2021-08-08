import sys

n = int(sys.stdin.readline())
steps = [0 for i in range(301)]
score = [0 for i in range(301)]

for i in range(n):
    steps[i] = int(sys.stdin.readline())


score[0] = steps[0]
score[1] = steps[0] + steps[1]
score[2] = max(steps[0] + steps[2], steps[1] + steps[2])

for i in range(3, n):
    score[i] = max(score[i - 3] + steps[i - 1] + steps[i], score[i - 2] + steps[i])

print(score[n - 1])
