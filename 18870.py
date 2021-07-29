import sys

_ = sys.stdin.readline()
nums = sys.stdin.readline().split()
nums = list(map(int, nums))

unique = sorted(list(set([i for i in nums])))

dictionary = dict()

for i in range(len(unique)):
    dictionary[unique[i]] = i

string = ""

for n in nums:
    string += str(dictionary[n])
    string += " "

print(string[:-1])