import heapq
from collections import Counter, defaultdict

N = int(input().strip())
array = list(map(int, input().strip().split()))
num2index = defaultdict(list)
for i, num in enumerate(array):
    num2index[num].append(i)
counter = [[key, value] for key, value in Counter(array).items()]
heapq.heapify(counter)
while counter:
    key, times = heapq.heappop(counter)
    if times == 1:
        continue
    elif times == 2:
        for i, x in enumerate(counter):
            if x[0] == key * 2:
                counter[i][1] += 1
                break
        else:
            heapq.heappush(counter, [key * 2, 1])
        num2index[key * 2].append(min(num2index[key]))
        num2index[key * 2].sort()
        del num2index[key]
    else:
        for i, x in enumerate(counter):
            if x[0] == key * 2:
                counter[i][1] += 1
                break
        else:
            heapq.heappush(counter, [key * 2, 1])
        heapq.heappush(counter, [key, times - 2])
        num2index[key * 2].append(min(num2index[key]))
        num2index[key * 2].sort()
        num2index[key] = num2index[key][1:]
        num2index[key].sort()
result = sorted(((num2index[key], key) for key in num2index))
result = [x[1] for x in result]
print(' '.join(map(str, result)))
