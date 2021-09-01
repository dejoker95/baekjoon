import sys


def push(heap, num):
    heap.append((abs(num), num))
    child = len(heap) - 1

    while child > 0:
        parent = (child - 1) // 2
        if heap[parent][0] < heap[child][0]:
            break
        elif heap[parent][0] == heap[child][0] and heap[parent][1] < heap[child][1]:
            break
        else:
            temp = heap[parent]
            heap[parent] = heap[child]
            heap[child] = temp
            child = parent


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
            if heap[child1][0] < heap[child2][0]:
                small = child1
            elif heap[child1][0] > heap[child2][0]:
                small = child2
            elif heap[child1][1] < heap[child2][1]:
                small = child1
            else:
                small = child2
        if heap[parent][0] < heap[small][0]:
            break
        elif heap[parent][0] == heap[small][0] and heap[parent][1] <= heap[small][1]:
            break
        temp = heap[parent]
        heap[parent] = heap[small]
        heap[small] = temp
        parent = small
    return result


N = int(sys.stdin.readline())
heap = []
for i in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            a = pop(heap)
            print(a[1])
    else:
        push(heap, num)
