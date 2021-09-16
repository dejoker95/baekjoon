import sys

N, K = map(int, sys.stdin.readline().split())
use = list(map(int, sys.stdin.readline().split()))

plug = set()

ans = 0
for i in range(len(use)):
    if len(plug) < N:
        plug.add(use[i])
    elif use[i] in plug:
        continue
    else:
        late = -1
        late_plug = -1
        for p in plug:
            try:
                idx = use[i + 1 :].index(p)
                if late < idx:
                    late = idx
                    late_plug = p
            except:
                late_plug = p
                break

        plug.remove(late_plug)
        plug.add(use[i])
        ans += 1
print(ans)