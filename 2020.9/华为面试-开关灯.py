# n = 100
# lights = [False] * 100
# for i in range(1, n + 1):
#     for j in range(i - 1, len(lights), i):
#         lights[j] = not lights[j]
# count = 0
# for i in range(len(lights)):
#     if lights[i]:
#         count += 1
#         print(i + 1, end=' ')
# print()
# print(count)
from math import sqrt

print(int(sqrt(100)))