def find_bigger(sub, base, start, end):
    while start < end:
        mid = (end + start) // 2
        if sub[base][1] < sub[mid][0]:
            end = mid - 1
        else:
            start = mid + 1
    print(start)
    if start == base + 1:
        if sub[base][1] < sub[start][0]:
            return len(sub) - start
        else:
            return len(sub) - start - 1
    elif start == len(sub) - 1:
        if sub[base][1] < sub[start][0]:
            return 1
        else:
            return 0
    elif sub[base][1] < sub[start][0]:
        return len(sub) - start
    elif sub[base][1] < sub[start + 1][0]:
        return len(sub) - start - 1


def paperCuttings(textLength, starting, ending):
    # Write your code here
    sub = set()
    for i in range(len(starting)):
        sub.add((starting[i], ending[i]))
    sub = sorted(list(sub), key=lambda x: x[0])
    answer = 0
    for i in range(len(sub) - 1):
        answer += find_bigger(sub, i, i + 1, len(sub) - 1)

    return answer


# def paperCuttings(textLength, starting, ending):
#     # Write your code here
#     sub = set()
#     for i in range(len(starting)):
#         sub.add((starting[i], ending[i]))
#     sub = sorted(list(sub), key=lambda x: x[0])
#     answer = 0
#     for i in range(len(sub)):
#         for j in range(i + 1, len(sub)):
#             if sub[i][1] < sub[j][0]:
#                 answer += len(sub) - j
#                 break

#     return answer


textLength = 8

starting = [3, 4, 5, 6, 8]


ending = [4, 5, 6, 7, 8]

result = paperCuttings(textLength, starting, ending)
print(result)