from test_script import TreeNode
from test_script import TreeUtil


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return False
        iterator = TreeUtil.inOrderTraversalIterator(root)
        previous = next(iterator)
        for node in iterator:
            if node.val <= previous.val:
                return False
            previous = node
        return True


print(Solution().isValidBST(TreeUtil.createBinaryTree([10, 5, 15, None, None, 6, 20])))
