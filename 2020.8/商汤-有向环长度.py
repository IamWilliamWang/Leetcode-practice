#
# 计算图中环的长度。
# @param input int整型一维数组 按题目描述中表达的图
# @return int整型
#
class Solution:
    def CalculateLength(self, inputStr: list):
        queue = [0]
        path = {}
        i = 0
        while queue:
            node = queue.pop(0)
            if node in path:
                return i - path[node]
            path[node] = i
            i += 1
            queue.append(inputStr[node])
        return 0


print(Solution().CalculateLength([1, 2, 3, 0]))
