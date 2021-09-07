import sys
import heapq


class Heap:
    def __init__(self):
        self.median = None
        self.minHeap = []
        self.maxHeap = []

    def push(self, num):
        if self.median == None:
            self.median = num
            return

        if self.median < num:
            heapq.heappush(self.minHeap, num)
        else:
            heapq.heappush(self.maxHeap, -num)

        if len(self.minHeap) - len(self.maxHeap) <= -1:
            pop = -heapq.heappop(self.maxHeap)
            heapq.heappush(self.minHeap, self.median)
            self.median = pop
        elif len(self.minHeap) - len(self.maxHeap) >= 2:
            pop = heapq.heappop(self.minHeap)
            heapq.heappush(self.maxHeap, -self.median)
            self.median = pop


if __name__ == "__main__":
    heap = Heap()
    N = int(sys.stdin.readline())

    for i in range(N):
        num = int(sys.stdin.readline())
        heap.push(num)
        print(heap.median)
