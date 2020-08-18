#
#
# @param arr int整型一维数组
# @return bool布尔型
#
class Solution:
    def Game24Points(self, arr):
        def dfs(i: int, num: float):
            if i >= len(arr):
                if num == 24:
                    return True
                return False
            return dfs(i + 1, num + arr[i]) or dfs(i + 1, num - arr[i]) or dfs(i + 1, num * arr[i]) or dfs(i + 1,
                                                                                                           num / arr[i])

        return dfs(1, arr[0])
