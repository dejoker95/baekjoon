import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
T = list(map(int, sys.stdin.readline().split()))


A.sort()


def binary_search(A, start, end, target):
    if start >= end:
        if A[start] == target:
            return 1
        else:
            return 0

    mid = (start + end) // 2 + 1

    if target == A[mid]:
        return 1
    elif target < A[mid]:
        return binary_search(A, start, mid - 1, target)
    else:
        return binary_search(A, mid, end, target)


for t in T:
    print(binary_search(A, 0, len(A) - 1, t))
