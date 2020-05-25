from typing import List


class Solution:
    def _getEstimatedIndexRange(self, nums: List[int], target: int) -> (int, int):
        if nums[0] > target:  # 一直向左寻找范围
            rightIndex = 0
            leftIndexes = [-len(nums) // 2]
            while nums[leftIndexes[-1]] >= target and leftIndexes[-1] != rightIndex:
                if len(leftIndexes) > 1 and leftIndexes[-1] == leftIndexes[-2]:
                    return leftIndexes[-1] + 1, rightIndex - 1
                if nums[leftIndexes[-1]] == target:
                    return leftIndexes[-1], leftIndexes[-1]
                if nums[leftIndexes[-1]] > nums[rightIndex]:  # 飙过头了
                    leftIndexes.append(int((leftIndexes[-1] + rightIndex) / 1.5))
                    if leftIndexes[-1] == leftIndexes[-2]:
                        leftIndexes[-1] += 1
                    continue
                if nums[leftIndexes[-1]] > target:  # 范围不够广
                    leftIndexes.append(int(leftIndexes[-1] * 1.5))
                    if leftIndexes[-1] < -len(nums):
                        leftIndexes[-1] = -len(nums)
                    if leftIndexes[-1] == leftIndexes[-2] and leftIndexes[-1] > -len(nums):
                        leftIndexes[-1] -= 1
                    continue
            leftIndex = leftIndexes[-1]
        elif nums[0] < target:  # 一直向右寻找范围
            leftIndexes = [0]
            rightIndexes = [len(nums) // 2]
            while nums[rightIndexes[-1]] <= target and leftIndexes[-1] != rightIndexes[-1]:
                if len(rightIndexes) > 1 and rightIndexes[-1] == rightIndexes[-2]:
                    return leftIndexes[-1] + 1, rightIndexes[-1] - 1
                if nums[leftIndexes[-1]] == target:
                    return leftIndexes[-1], leftIndexes[-1]
                if nums[rightIndexes[-1]] == target:
                    return rightIndexes[-1], rightIndexes[-1]
                if nums[leftIndexes[-1]] > nums[rightIndexes[-1]]:  # 飙过头了
                    rightIndexes.append(int((leftIndexes[-1] + rightIndexes[-1]) / 1.5))
                    if rightIndexes[-1] == rightIndexes[-2]:
                        rightIndexes[-1] -= 1
                    continue
                if nums[rightIndexes[-1]] < target:  # 范围不够广
                    leftIndexes.append(rightIndexes[-1])
                    rightIndexes.append(int(rightIndexes[-1] * 1.5))
                    if rightIndexes[-1] >= len(nums):
                        rightIndexes[-1] = len(nums) - 1
                    if rightIndexes[-1] == rightIndexes[-2] and rightIndexes[-1] < len(nums) - 1:
                        rightIndexes[-1] += 1
                    continue
            leftIndex, rightIndex = leftIndexes[-1], rightIndexes[-1]
        else:
            leftIndex, rightIndex = 0, 0
        return leftIndex, rightIndex

    def _binarySearch(self, nums: List[int], target: int, leftIndex: int, rightIndex: int) -> int:
        while leftIndex <= rightIndex:
            mid = (leftIndex + rightIndex) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                rightIndex = mid - 1
            else:
                leftIndex = mid + 1
        return 1000000000

    def slowSearch(self, nums: List[int], target: int) -> int:
        # if len(nums) < 1000:
        #     return nums.index(target) if target in nums else -1
        if not nums:
            return -1
        leftBorder, rightBorder = self._getEstimatedIndexRange(nums, target)
        if leftBorder > rightBorder:
            return -1
        foundIndex = self._binarySearch(nums, target, leftBorder, rightBorder)
        if foundIndex == 1000000000:
            return -1
        return foundIndex + len(nums) if foundIndex < 0 else foundIndex

    def search(self, nums: List[int], target: int) -> int:
        if len(nums) < 2:
            return nums.index(target) if target in nums else -1
        leftBorder = 0
        rightBorder = len(nums) - 1
        while leftBorder <= rightBorder:
            mid = (leftBorder + rightBorder) // 2
            if nums[mid] == target:
                return mid
            # 只处理顺序排列的一半，另一半不管
            if nums[0] < nums[mid]:  # 左侧是顺序排列的
                if nums[0] <= target <= nums[mid - 1]:
                    rightBorder = mid - 1
                else:
                    leftBorder = mid + 1
            else:  # 右侧是顺序排列的
                if nums[mid + 1] <= target <= nums[-1]:
                    leftBorder = mid + 1
                else:
                    rightBorder = mid - 1
        return -1


# print(Solution().search(
#     nums=[20, 21, 23, 24, 27, 31, 32, 34, 35, 37, 40, 42, 43, 44, 45, 49, 50, 51, 53, 55, 56, 58, 60, 62, 68, 70, 73,
#           76, 79, 80, 81, 83, 85, 95, 96, 97, 101, 103, 105, 107, 108, 114, 115, 123, 127, 128, 130, 133, 135, 136, 144,
#           146, 149, 153, 154, 157, 158, 159, 160, 161, 166, 173, 175, 177, 179, 180, 184, 185, 193, 195, 196, 197, 198,
#           200, 203, 205, 207, 208, 209, 211, 213, 214, 215, 216, 217, 218, 220, 224, 226, 227, 228, 229, 230, 233, 234,
#           240, 245, 246, 252, 253, 254, 255, 256, 257, 259, 270, 271, 272, 279, 282, 283, 284, 288, 291, 292, 293, 294,
#           296, 5, 6, 7, 9, 15]
#     , target=273))
print(Solution().search(nums=[3,5,1], target=0))
