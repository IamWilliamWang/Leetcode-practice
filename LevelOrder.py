from typing import List
from test_script import TreeNode, TreeUtil

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        return TreeUtil.breadthFirstTraversal(root)
