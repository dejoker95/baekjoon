import sys
from collections import defaultdict

N = int(sys.stdin.readline())
crain = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
box = list(map(int, sys.stdin.readline().split()))


crain.sort(reverse=True)
box.sort(reverse=True)
done = [0] * len(box)

if crain[0] < box[0]:
    print(-1)
else:
    canLift = defaultdict(list)
    for i in range(len(crain)):
        for j in range(len(box)):
            if crain[i] >= box[j]:
                canLift[crain[i]].append(j)

    ans = 0
    count = 0
    while count < len(box):
        ans += 1
        for i in range(len(crain)):
            for j in canLift[crain[i]]:
                if done[j] == 0:
                    done[j] = 1
                    count += 1
                    break

    print(ans)
