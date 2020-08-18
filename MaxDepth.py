from test_script import TreeNode, TreeUtil


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return TreeUtil.maxLevel(root)
