from itertools import product

N = int(input().strip())
maxPoints = list(map(int, input().strip().split()))[:N]
result = []
for pointsTuple in product(*[range(1, maxPoint + 1) for maxPoint in maxPoints]):
    result.append(max(pointsTuple))
print('%.2f' % (sum(result) / len(result)))
