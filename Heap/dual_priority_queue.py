import heapq as hq


def solution(operations):
    heap = []
    max_heap = []
    for op in operations:
        if op == "D -1":
            if heap:
                num = hq.heappop(heap)
                max_heap.remove(-num)
        elif op == "D 1":
            if heap:
                num = hq.heappop(max_heap)
                heap.remove(-num)
        else:
            op = op.split(" ")
            num = int(op[-1])
            hq.heappush(heap, num)
            hq.heappush(max_heap, -num)

    if heap:
        return [max(heap), min(heap)]
    else:
        return [0, 0]


operations = ["I 16", "D 1"]
print(solution(operations))