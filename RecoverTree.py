from test_script import TreeNode, TreeUtil


class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        inorderNodes = []
        for node in TreeUtil.inOrderTraversalIterator(root):
            inorderNodes.append((node.val, node))
        strangeNums = []
        for i in range(1, len(inorderNodes) - 1):
            if not inorderNodes[i - 1][0] < inorderNodes[i][0] < inorderNodes[i + 1][0]:
                strangeNums.append(inorderNodes[i])
        assert len(strangeNums) == 2
        exch1, exch2 = strangeNums
        exch1[1].val, exch2[1].val = exch2[1].val, exch1[1].val


root = TreeUtil.createTreeByPreInOrder([1, 3, 2], [3, 2, 1])
Solution().recoverTree(root)
print(root)
root = TreeUtil.createTreeByPreInOrder([3, 1, 4, 2], [1, 3, 2, 4])
