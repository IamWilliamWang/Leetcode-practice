class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def makeRoot():
    global array, i
    if array[i] == -1:
        i += 1
        return None
    root = TreeNode(array[i])
    i += 1
    root.left = makeRoot()
    root.right = makeRoot()
    return root


def findAncestor(root: TreeNode) -> int:
    if not root:
        return
    if root.val == find1:
        return find1
    if root.val == find2:
        return find2
    left = findAncestor(root.left)
    right = findAncestor(root.right)
    if left and right:
        return root.val
    if not left and not right:
        return
    if not left:
        return right
    if not right:
        return left


array = list(map(int, input().strip().split()))
i = 0
root = makeRoot()
find1, find2 = list(map(int, input().strip().split()))
print(findAncestor(root))
