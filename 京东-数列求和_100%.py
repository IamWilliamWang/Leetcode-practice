import sys

n = int(input().strip())
ans = 0
plus, minus = 5, 10
for i in range(n):
    ans = ans + 1 / plus - 1 / minus
    plus, minus = plus + 10, minus + 10
sys.stdout.write('%.4f' % ans)
