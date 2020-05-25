class Solution:
    def permute(self, nums: list) -> list:
        if len(nums) == 0:
            return [[]]
        result = []
        for firstNum in nums:
            nextNums = nums.copy()
            nextNums.remove(firstNum)
            matrix = self.permute(nextNums)
            for i in range(len(matrix)):
                matrix[i].insert(0, firstNum)
            result += matrix
        return result


print(Solution().permute([]))
