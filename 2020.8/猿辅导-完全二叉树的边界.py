N = int(input().strip())
heap = list(map(int, input().strip().split()))
result = []
level = 0
while 2 ** level - 1 < len(heap):
    result.append(heap[2 ** level - 1])
    level += 1
level -= 1
result += heap[2 ** level:]
result += heap[len(heap) // 2:2 ** level - 1]
while heap and 2 ** level - 2 > 0:
    if heap[2 ** level - 2] not in result:
        result.append(heap[2 ** level - 2])
    level -= 1
print(' '.join(map(str, result)))
