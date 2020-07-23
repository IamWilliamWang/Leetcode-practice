from typing import List
from test_script import TreeNode
from functools import lru_cache
from itertools import product


class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        @lru_cache(maxsize=None)
        def dp(start: int, end: int) -> List[TreeNode]:
            if end - start == 1:
                return [TreeNode(start)]
            if end - start < 1:
                return []
            roots = []
            for centerI in range(start, end):
                allLefts = dp(start, centerI)
                allRights = dp(centerI + 1, end)
                if not allLefts:
                    allLefts = [None]
                if not allRights:
                    allRights = [None]
                for leftTree, rightTree in product(allLefts, allRights):
                    nowRoot = TreeNode(centerI)
                    nowRoot.left = leftTree
                    nowRoot.right = rightTree
                    roots.append(nowRoot)
            return roots
        return dp(1, n + 1)
