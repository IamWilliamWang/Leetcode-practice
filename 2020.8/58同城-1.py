#
#
# @param values string字符串二维数组
# @return string字符串一维数组
#
class Solution:
    def findCommonString(self, values):
        if not values:
            return []
        values.sort()
        commonSet = set(values[0])
        for i in range(1, len(values)):
            commonSet.intersection_update(values[i])
        result = []
        for num in sorted(values)[0]:
            if num in commonSet:
                result.append(num)
        return result
