import sys
import heapq

N = int(sys.stdin.readline())

heap = []

for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap, num)

"""
직접 구현한 힙

def push(heap, num):
    heap.append(num)
    child = len(heap) - 1

    while child > 0:
        parent = (child - 1) // 2
        if heap[parent] > heap[child]:
            temp = heap[parent]
            heap[parent] = heap[child]
            heap[child] = temp
            child = parent
        else:
            break



def pop(heap):

    result = heap[0]
    heap[0] = heap[-1]
    heap.pop()

    parent = 0
    while True:
        child1 = parent * 2 + 1
        child2 = parent * 2 + 2
        small = 0
        if child1 >= len(heap):
            break
        elif child2 >= len(heap):
            small = child1
        else:
            small = child1 if heap[child1] <= heap[child2] else child2

        if heap[small] >= heap[parent]:
            break
        temp = heap[parent]
        heap[parent] = heap[small]
        heap[small] = temp
        parent = small

    return result


for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(pop(heap))
    else:
        push(heap, num)
"""
