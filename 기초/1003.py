import sys

T = int(sys.stdin.readline())


def fibonacci(n):
    global count

    if n in count:
        return count[n]
    else:
        a1 = fibonacci(n - 1)
        a2 = fibonacci(n - 2)
        answer = [a1[0] + a2[0], a1[1] + a2[1]]
        count[n] = answer
        return answer


test = []
for _ in range(T):
    test.append(int(sys.stdin.readline()))

for t in test:
    count = {0: [1, 0], 1: [0, 1]}
    result = fibonacci(t)
    print(result[0], result[1])
