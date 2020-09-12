#
#
# @param intervals int整型二维数组
# @return int整型
#
from collections import defaultdict


class Solution:
    def eraseOverlapIntervals(self, intervals):
        orders = []
        for interval in intervals:
            orders += [(interval[0], True), (interval[1], False)]
        orders.sort()
        use = defaultdict(int)
        for orderTime, orderType in orders:
            if orderType:
                use[orderTime] += 1
            else:
                use[orderTime] -= 1
        using = 0
        ans = 0
        for num in use.values():
            using += num
            ans = max(ans, using)
        return ans - 1


print(Solution().eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
