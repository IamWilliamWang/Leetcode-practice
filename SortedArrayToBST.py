from typing import List

from test_script import TreeNode


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        root = TreeNode(nums[len(nums) // 2])
        root.left = self.sortedArrayToBST(nums[:len(nums) // 2])
        if len(nums) > 2:
            root.right = self.sortedArrayToBST(nums[len(nums) // 2 + 1:])
        return root


print(Solution().sortedArrayToBST([-10, -3, 0, 5, 9]))
