import sys

days, count = list(map(int, sys.stdin.readline().strip().split()))
a1 = int(0.5 * count / (1 - 2 ** (-days)))
print(a1)
