from test_script import TreeNode, TreeUtil


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if t is None:
            return s is None

        for subRootS in TreeUtil.postOrderTraversalIterator(s):
            if subRootS.val != t.val or TreeUtil.maxLevel(subRootS) != TreeUtil.maxLevel(t):
                continue
            if TreeUtil.preOrderTraversal(subRootS) == TreeUtil.preOrderTraversal(t) \
                    and TreeUtil.inOrderTraversal(subRootS) == TreeUtil.inOrderTraversal(t):
                return True
        return False


print(Solution().isSubtree(TreeUtil.createBinaryTree([1, 2, 3]), TreeUtil.createBinaryTree([2, 3])))
