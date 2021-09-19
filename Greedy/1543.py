S = input().strip()
s = input().strip()


def check(s, S, idx):
    if len(S) - idx < len(s):
        return False
    for c in s:
        if c != S[idx]:
            return False
        idx += 1
    return True


i = 0
ans = 0
while i < len(S):
    r = check(s, S, i)
    if r == False:
        i += 1
    else:
        ans += 1
        i += len(s)

print(ans)