from typing import Dict

from test_script import TreeNode


class Solution:
    def recoverFromPreorder(self, S: str) -> TreeNode:
        def next():
            nonlocal i
            if i == len(S):
                return -1, -1
            level = 0
            while S[i] == '-':
                level += 1
                i += 1
            end = S.find('-', i)
            if end == -1:
                end = len(S)
            number = S[i:end]
            i = end
            return int(number), level

        if not S:
            return None
        i: int = S.find('-')
        if i == -1:
            i = len(S)
        root = TreeNode(S[0:i])
        child2Parent: Dict[TreeNode, TreeNode] = {}
        nowPointer: TreeNode = root
        nowLevel: int = 0
        while True:
            newVal, newLevel = next()
            if newLevel == -1:
                break
            while nowLevel + 1 > newLevel:
                nowPointer = child2Parent[nowPointer]
                nowLevel -= 1
            if nowLevel + 1 == newLevel:
                if nowPointer.left is None:
                    nowPointer.left = TreeNode(newVal)
                    child2Parent[nowPointer.left] = nowPointer
                    nowPointer = nowPointer.left
                    nowLevel += 1
                else:
                    nowPointer.right = TreeNode(newVal)
                    child2Parent[nowPointer.right] = nowPointer
                    nowPointer = nowPointer.right
                    nowLevel += 1
        return root


print(Solution().recoverFromPreorder("1-2--3---4-5--6---7"))
