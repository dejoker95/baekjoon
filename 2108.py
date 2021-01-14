import sys
from collections import Counter

case = int(sys.stdin.readline())
num_list = []
for i in range(case):
    num_list.append(int(sys.stdin.readline()))
num_list.sort()

print(round(sum(num_list)/case))
print(num_list[case//2])

count = Counter(num_list).most_common()

if case == 1:
    print(num_list[0])
else:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])

print(num_list[-1] - num_list[0])