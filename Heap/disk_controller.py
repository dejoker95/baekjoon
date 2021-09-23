import heapq as hq


def solution(jobs):
    heap = []
    jobs.sort(key=lambda x: x[0])
    t = 0
    total = 0
    idx = 0
    work_until = 0
    while True:
        if idx == len(jobs) and len(heap) == 0:
            break

        while idx < len(jobs) and t >= jobs[idx][0]:
            hq.heappush(heap, (jobs[idx][1], jobs[idx][0]))
            idx += 1

        if heap and t >= work_until:
            j = hq.heappop(heap)
            work_until = t + j[0]
            total += work_until - j[1]
            t = work_until
        else:
            t += 1

    return total // len(jobs)


jobs = [[0, 3], [1, 9], [2, 6]]
print(solution(jobs))