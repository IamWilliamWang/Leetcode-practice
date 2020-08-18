import heapq
import sys

n, m, x = list(map(int, input().strip().split()))
arr = list(map(int, input().strip().split()))[:n]
arrLen, medicineCount, medicineGrow = n, m, x
heapq.heapify(arr)
for _ in range(medicineCount):
    minGrass = heapq.heappop(arr)
    minGrass += medicineGrow
    heapq.heappush(arr, minGrass)
sys.stdout.write(str(heapq.heappop(arr)))
