import sys


def check_two(string, left, right):
    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            return False
    return True


def check(string, left, right):

    while left < right:
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            check1 = check_two(string, left + 1, right)
            check2 = check_two(string, left, right - 1)
            if check1 or check2:
                return 1
            else:
                return 2
    return 0


T = int(sys.stdin.readline())

for i in range(T):
    string = sys.stdin.readline().strip()
    print(check(string, 0, len(string) - 1))
