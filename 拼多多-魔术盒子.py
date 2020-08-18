import math

N = int(input().strip())
for _ in range(N):
    num = int(input().strip())
    print(int(math.log2(num)) + 1)
