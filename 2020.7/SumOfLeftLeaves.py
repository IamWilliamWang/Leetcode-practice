from test_script import TreeNode, TreeUtil


class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        leftValSum = 0
        for node in TreeUtil.preOrderTraversalIterator(root):
            if node.left and node.left.left is None and node.left.right is None:
                leftValSum += node.left.val
        return leftValSum
[1,2,3,4,5]