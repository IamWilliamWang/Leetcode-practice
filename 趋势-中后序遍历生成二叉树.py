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


def create(inorder: str, postorder: str):
    if not inorder or not postorder:
        return None
    if len(inorder) != len(postorder):
        return None
    root = TreeNode(postorder[-1])
    inorderRootIdx = inorder.index(root.val)
    leftTreeInorder = inorder[:inorderRootIdx]
    rightTreeInorder = inorder[inorderRootIdx + 1:]
    leftTreePostorder = postorder[:-1 - len(rightTreeInorder)]
    rightTreePostorder = postorder[-1 - len(rightTreeInorder):-1]
    root.left = create(leftTreeInorder, leftTreePostorder)
    root.right = create(rightTreeInorder, rightTreePostorder)
    return root


inorder, postorder = input().strip().split()
root = create(inorder, postorder)
for node in preOrderTraversalIterator(root):
    print(node.val, end='')
