import heapq

n, m, k = list(map(int, input().strip().split()))
heap = []
for i in range(1, n + 1):
    for j in range(1, m + 1):
        heap.append(i * j)
heapq.heapify(heap)
if k < n * m / 2:
    print(heapq.nlargest(k, heap)[-1])
else:
    print(heapq.nsmallest(len(heap) - k + 1, heap)[-1])
