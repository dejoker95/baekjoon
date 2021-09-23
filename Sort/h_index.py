def solution(citations):
    H = 0
    citations.sort(reverse=True)

    for i in range(len(citations)):
        H = max(H, min(i + 1, citations[i]))

    return H