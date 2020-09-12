#
# 找到比输入的整数大的下一个水仙花数
# @param n int整型 输入的整数
# @return long长整型
#
from math import log10


class Solution:
    def nextNarcissisticNumber(self, n):
        def length(number: int):
            return int(log10(number)) + 1

        num = n + 1
        while True:
            if num == sum((int(x) ** length(num) for x in str(num))):
                break
            num += 1
        return num


print(Solution().nextNarcissisticNumber(108))
