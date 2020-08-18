from test_script import TreeNode, TreeUtil, speedtest, standard


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        allNodes = list(TreeUtil.preOrderTraversalIterator(root))
        for i in range(len(allNodes) - 1):
            allNodes[i].left = None
            allNodes[i].right = allNodes[i + 1]
        if root:
            allNodes[-1].left = allNodes[-1].right = None


speedtest(standard(Solution().flatten, None), [None])
