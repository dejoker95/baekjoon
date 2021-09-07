import sys


while True:
    hist = list(map(int, sys.stdin.readline().split()))
    if hist[0] == 0:
        break

    ans = 0
    stack = [[0, 0]]
    hist.append(0)

    for i in range(1, hist[0] + 2):
        while stack[-1][1] > hist[i]:
            tmp_hist = stack.pop()
            tmp_area = 0
            while stack[-1][1] == tmp_hist[1]:
                stack.pop()
            tmp_area = max(
                (i - 1 - stack[-1][0]) * tmp_hist[1], (i - tmp_hist[0]) * tmp_hist[1]
            )
            if tmp_area > ans:
                ans = tmp_area
        stack.append([i, hist[i]])

    print(ans)
