from typing import List
from test_script import TreeNode, TreeUtil


class Solution:
    def isGoodNode(self, heap: List[object], index: int) -> bool:
        """
        使用heap判断第index个节点是否为好节点
        :param heap: 保存节点内容的堆（1-based index）
        :param index: 第index个节点（1-based index）
        :return:
        """
        nowNumber = heap[index]
        while index > 0:
            if heap[index] > nowNumber:
                return False
            index //= 2  # 找父亲节点
        return True

    def goodNodes(self, root: TreeNode) -> int:
        heap = TreeUtil.toValHeap(root)
        heap = [None] + heap
        count = 0
        for i in range(1, len(heap)):
            if heap[i] is not None and self.isGoodNode(heap, i):
                count += 1
        return count


tree = TreeUtil.createBinaryTree([-5, -1, -4, None, None, -5, 0, None, None, None, None, -5, None, -1, 2])
tree.right.right.left.right = TreeUtil.createBinaryTree([-3, None, -5, None, None, None, -4])
print(Solution().goodNodes(tree))
