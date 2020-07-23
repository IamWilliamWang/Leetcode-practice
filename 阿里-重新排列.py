# 重新排列
import itertools
import sys

n = int(sys.stdin.readline().strip())
for series in itertools.permutations(range(1, n + 1)):
    vaild = True
    for i in range(1, len(series)):
        if abs(series[i] - series[i - 1]) == 1:
            vaild = False
            break
    if vaild:
        print(' '.join(map(str, series)))
