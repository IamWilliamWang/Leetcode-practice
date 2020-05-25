# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


from functools import lru_cache
class Solution:
    def _getVal(self, node: TreeNode):
        return node.val if node is not None else 0

    def _traverseTree(self, root: TreeNode):
        from math import log
        self._nodeList = []
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)
            self._nodeList.append(node)
            if node is None:
                continue
            queue.append(node.left)
            queue.append(node.right)
        while self._nodeList[-1] is None:
            self._nodeList.pop()
        self._maxLevel = int(log(len(self._nodeList), 2)) + 1
        nodeListLenShouldBe = 2 ** self._maxLevel - 1
        for i in range(nodeListLenShouldBe - len(self._nodeList)):
            self._nodeList.append(None)

    def levelSum(self, level: int) -> int:
        startIndex = 2 ** (level - 1) - 1
        if startIndex == 0:
            return self._getVal(self._nodeList[0])
        levelLen = 2 ** level - 2 ** (level - 1)
        sum = 0
        for i in range(startIndex, startIndex + levelLen):
            sum += self._getVal(self._nodeList[i])
        return sum

    def rob(self, root: TreeNode) -> int:
        # self._traverseTree(root)
        # sum1, sum2 = 0, 0
        # for i in range(1, self._maxLevel, 2):
        #     sum1 += self.levelSum(i)
        # for i in range(2, self._maxLevel, 2):
        #     sum2 += self.levelSum(i)
        # return max(sum1, sum2)
        @lru_cache(maxsize=None)
        def dfs(node: TreeNode, skipFlag: bool) -> int:
            if node is None:
                return 0
            if skipFlag:
                return dfs(node.left, False) + dfs(node.right, False)
            else:
                return max(dfs(node.left, False) + dfs(node.right, False),
                           node.val + dfs(node.left, True) + dfs(node.right, True))

        return max(dfs(root, True), dfs(root, False))

root = TreeNode(3)
node1 = TreeNode(4)
node2 = TreeNode(5)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.right = node5
print(Solution().rob(root))
