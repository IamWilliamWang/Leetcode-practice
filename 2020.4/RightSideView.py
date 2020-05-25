# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def rightSideView(self, root: TreeNode) -> list:
        level2Nums = {}
        def traverseTree(node: TreeNode, level: int):
            if node is None:
                return
            if level not in level2Nums:
                level2Nums[level] = [node.val]
            else:
                level2Nums[level].append(node.val)
            traverseTree(node.left, level + 1)
            traverseTree(node.right, level + 1)
        traverseTree(root, 1)
        dictList = list(level2Nums.items())
        dictList.sort()
        result = []
        for level, valList in dictList:
            result.append(valList[-1])
        return result

root=TreeNode(1)
left=TreeNode(2)
leftRight=TreeNode(5)
right=TreeNode(3)
rightRight=TreeNode(4)
# root.left=left
root.right=right
left.right=leftRight
right.right=rightRight
print(Solution().rightSideView(root))
