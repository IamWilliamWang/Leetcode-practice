from test_script import TreeNode, TreeUtil


class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def equals(root1: TreeNode, root2: TreeNode):
            if not root2:
                return True
            if not root1:
                return False
            return root1.val == root2.val and equals(root1.left, root2.left) and equals(root1.right, root2.right)

        if not A or not B:
            return False
        return equals(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)


print(Solution().isSubStructure(TreeUtil.createTreeByPreInOrder([3, 4, 1, 2, 5], [1, 4, 2, 3, 5]),
                                TreeUtil.createTreeByHeap([4, 1])))
