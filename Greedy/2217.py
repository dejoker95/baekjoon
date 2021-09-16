N = int(input())

rope = [int(input()) for i in range(N)]
rope.sort()
ans = -1

for i in range(N):
    w = rope[i] * (N - i)
    if w > ans:
        ans = w
print(ans)
