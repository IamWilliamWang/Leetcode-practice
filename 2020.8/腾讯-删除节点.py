N, idx = list(map(int, input().strip().split()))
array = list(map(int, input().strip().split()))
del array[idx - 1]
print(' '.join(map(str, array)))
