from test_script import TreeNode, TreeUtil, speedtest
import math


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        heap = TreeUtil.toValHeap(root)
        maxLevel = int(math.log2(len(heap) + 1))
        for level in range(1, maxLevel + 1):
            indexBegin = 2 ** (level - 1) - 1
            indexEnd = 2 ** level - 1 - 1
            while indexBegin < indexEnd:
                if heap[indexBegin] != heap[indexEnd]:
                    return False
                indexBegin += 1
                indexEnd -= 1
        return True

    def isSymmetric_fast(self, root: TreeNode) -> bool:
        def equals(node1: TreeNode, node2: TreeNode):
            if not node1 and not node2:
                return True
            elif (node1 and node2) is None:
                return False
            return node1.val == node2.val and equals(node1.left, node2.right) and equals(node1.right, node2.left)

        if not root:
            return True
        return equals(root.left, root.right)


speedtest([Solution().isSymmetric, Solution().isSymmetric_fast], [
    TreeUtil.createTreeByPreInOrder([1, 2, 4, 6, 5, 7, 9, 10, 8, 3, 5, 8, 7, 9, 10, 4, 6],
                                    [4, 6, 2, 7, 10, 9, 5, 8, 1, 8, 5, 9, 10, 7, 3, 6, 4])])
speedtest([Solution().isSymmetric, Solution().isSymmetric_fast], [
    TreeUtil.createTreeByPreInOrder([1, 2, 4, 6, 5, 7, 9, 10, 8, 2, 5, 8, 7, 9, 10, 4, 6],
                                    [4, 6, 2, 7, 10, 9, 5, 8, 1, 8, 5, 9, 10, 7, 2, 6, 4])])
