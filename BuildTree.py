from typing import List
from test_script import TreeNode, TreeUtil


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return TreeUtil.createTreeByPreInOrder(preorder, inorder)


print(str(Solution().buildTree(preorder=[3, 9, 20, 15, 7], inorder=[9, 3, 15, 20, 7])))
