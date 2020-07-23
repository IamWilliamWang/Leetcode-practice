import threading

from test_script import TreeNode, TreeUtil, timer


class Codec:
    def serialize(self, root: TreeNode) -> str:
        """
        Encodes a tree to a single string.
        """
        return str(TreeUtil.toValHeapToDict(root)).replace(' ', '')

    @timer
    def deserialize(self, data: str) -> TreeNode:
        """
        Decodes your encoded data to tree.
        """
        return TreeUtil.createTreeByHeapExpressedByDict(eval(data))


root = TreeUtil.createTreeByPreInOrder(list(range(1, 1001)), list(range(1, 1001)))
treeDictStr = Codec().serialize(root)
Codec().deserialize(treeDictStr)
print(treeDictStr)
