#
#
# @param a int整型
# @param b int整型
# @return int整型
#
from math import sqrt


class Solution:
    def question(self, a, b):
        squares_all = [i ** 2 for i in range(int(sqrt(900)) + 1)]
        for s_num in squares_all:
            k = s_num - a
            if k <= 0:
                continue
            if k + b in squares_all:
                return k
        return -1
