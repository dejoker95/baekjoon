import sys
import math

n = int(sys.stdin.readline())


dot = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]
dot.sort()


def distance(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


def solve(start, end):
    if start == end:
        return math.inf

    else:
        mid = (start + end) // 2
        result = min(solve(start, mid), solve(mid + 1, end))

        candidate = []

        for i in range(mid, start - 1, -1):
            if (dot[i][0] - dot[mid][0]) ** 2 < result:
                candidate.append(dot[i])
            else:
                break
        for i in range(mid + 1, end + 1):
            if (dot[i][0] - dot[mid][0]) ** 2 < result:
                candidate.append(dot[i])
            else:
                break

        candidate.sort(key=lambda x: x[1])

        for i in range(len(candidate) - 1):
            for j in range(i + 1, len(candidate)):
                if (candidate[i][1] - candidate[j][1]) ** 2 < result:
                    result = min(result, distance(candidate[i], candidate[j]))
                else:
                    break

        return result


if len(dot) != len((set(dot))):
    print(0)
else:
    print(solve(0, len(dot) - 1))
