from test_script import TreeNode, TreeUtil


class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dp(node: TreeNode):
            if node is None:
                return 0
            leftMax = max(dp(node.left), 0)
            rightMax = max(dp(node.right), 0)
            nonlocal maxResult
            maxResult = max(maxResult, node.val + leftMax + rightMax)
            return node.val + max(leftMax, rightMax)

        maxResult = -2 ** 31
        return max(dp(root), maxResult)
