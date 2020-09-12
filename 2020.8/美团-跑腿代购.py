import heapq

count订单, count接单数 = list(map(int, input().strip().split()))
heap订单 = []
id = 1
for _ in range(count订单):
    value, weight = list(map(int, input().strip().split()))
    value += weight * 2
    heapq.heappush(heap订单, (-value, id))
    id += 1
result = []
for _ in range(min(count接单数, count订单)):
    _, id = heapq.heappop(heap订单)
    result.append(id)
print(' '.join(map(str, sorted(result))))
