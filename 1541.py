line = input()

minus = line.split("-")

minus_split = []


def add(line):
    line = list(map(int, line.split("+")))
    return sum(line)


for c in minus:
    if "+" in c:
        minus_split.append(add(c))
    else:
        minus_split.append(int(c))

result = minus_split[0]
for i in range(1, len(minus_split)):
    result -= minus_split[i]
print(result)