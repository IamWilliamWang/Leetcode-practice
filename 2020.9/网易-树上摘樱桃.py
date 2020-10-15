from collections import defaultdict


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def preOrderTraversalIterator(rootNode: TreeNode):
    """
    先序遍历，返回指向节点的迭代器
    :param rootNode 根节点
    :return: Iterator[TreeNode]
    """
    if rootNode is not None:
        yield rootNode
        yield from preOrderTraversalIterator(rootNode.left)
        yield from preOrderTraversalIterator(rootNode.right)


nodeCount, edgeCount = list(map(int, input().strip().split()))
relations = defaultdict(list)

for _ in range(edgeCount):
    fatherId, leftOrRight, childId = input().strip().split()
    fatherId, leftOrRight, childId = int(fatherId), 1 if leftOrRight == 'left' else 2, int(childId)
    relations[fatherId] += [(leftOrRight, childId)]

array = [None] * (nodeCount + 1)
for i in range(1, nodeCount + 1):
    array[i] = TreeNode(i)
childNode2FatherNode = {}
for id, values in relations.items():
    for type, childId in values:
        if type == 1:
            array[id].left = array[childId]
            childNode2FatherNode[array[childId]] = array[id]
        elif type == 2:
            array[id].right = array[childId]
            childNode2FatherNode[array[childId]] = array[id]
root = array[1]
resultSet = set()
for node in preOrderTraversalIterator(root):
    if not node.left and not node.right:
        fatherNode = childNode2FatherNode[node]
        if fatherNode.left is node and fatherNode.right:
            if not fatherNode.right.left and not fatherNode.right.right:
                resultSet.add(tuple(sorted([node.val, fatherNode.right.val])))
        elif fatherNode.right is node and fatherNode.left:
            if not fatherNode.left.left and not fatherNode.left.right:
                resultSet.add(tuple(sorted([node.val, fatherNode.left.val])))
print(len(resultSet))
