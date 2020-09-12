from test_script import Prime

from itertools import combinations

n, k = list(map(int, input().strip().split()))
array = sorted(map(int, input().strip().split()))[:n]
primes = Prime()
result = 0
for series in combinations(array, k):
    if sum(series) in primes:
        result += 1
print(result)
