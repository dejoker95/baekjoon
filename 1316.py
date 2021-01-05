n = int(input())

def check(word):
    c = set()
    prev = ''
    for char in word:
        if (char in c) and (prev != char):
            return False
        c.add(char)
        prev = char
    return True

count = 0
for i in range(n):
    word = input()
    if check(word) == True:
        count += 1
print(count)
