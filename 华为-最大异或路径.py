from collections import defaultdict


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, id: int, weight: int, leftId=-1, rightId=-1):
        self.id = id
        self.weight = weight
        self.leftId = leftId
        self.rightId = rightId


N = int(input().strip())
id2Node = {}
hasFatherIds = set()
for _ in range(N):
    id, weight, left, right = list(map(int, input().strip().split()))
    nownode = TreeNode(id, weight, left, right)
    id2Node[id] = nownode
    hasFatherIds.add(left)
    hasFatherIds.add(right)
rootId = list(set(id2Node.keys()).difference(hasFatherIds))[0]


def maxXorSum(id: int):
    def path(node: TreeNode):
        nonlocal maxNum
        if not node:
            return 0
        if node.leftId != -1:
            left = max(path(id2Node[node.leftId]), 0)
        else:
            left = 0
        if node.rightId != -1:
            right = max(path(id2Node[node.rightId]), 0)
        else:
            right = 0
        maxNum = max(maxNum, left ^ right ^ node.weight)
        return max(left ^ node.weight, right ^ node.weight)

    maxNum = -2 ** 31
    path(id2Node[id])
    return maxNum


print(maxXorSum(rootId))
