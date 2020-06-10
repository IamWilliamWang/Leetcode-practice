from test_script import TreeNode, TreeUtil, speedtest


class Solution:
    def longestConsecutive_clumsy(self, root: TreeNode) -> int:
        def detectLongestPath(root: TreeNode, valIs: int) -> int:
            if not root or root.val != valIs:
                return 0
            leftLongestPathLength = detectLongestPath(root.left, valIs + 1)
            rightLongestPathLength = detectLongestPath(root.right, valIs + 1)
            if leftLongestPathLength > rightLongestPathLength:
                return 1 + leftLongestPathLength
            else:
                return 1 + rightLongestPathLength

        longest = 0
        for node in TreeUtil.inOrderTraversalIterator(root):
            longestLocal = detectLongestPath(node, node.val)
            if longestLocal > longest:
                longest = longestLocal
        return longest

    def longestConsecutive(self, root: TreeNode) -> int:
        def detectLongestPath(root: TreeNode, valIs: int, nowLength: int) -> None:
            nonlocal longest
            if not root:
                return
            if root.val != valIs:
                nowLength = 1
                valIs = root.val
            else:
                nowLength += 1
            longest = max(longest, nowLength)
            detectLongestPath(root.left, valIs + 1, nowLength)
            detectLongestPath(root.right, valIs + 1, nowLength)

        longest = 0
        if not root:
            return 0
        detectLongestPath(root, root.val, 0)
        return longest


speedtest([Solution().longestConsecutive, Solution().longestConsecutive_clumsy],
          [TreeUtil.createTreeByPreInOrder([1, 3, 2, 4, 5], [1, 2, 3, 4, 5])])
speedtest([Solution().longestConsecutive, Solution().longestConsecutive_clumsy],
          [TreeUtil.createTreeByPreInOrder([2, 3, 2, 1], [2, 1, 2, 3])])
root = TreeNode(1)
node = root
for i in range(2, 5001):
    node.right = TreeNode(i)
    node = node.right
speedtest([Solution().longestConsecutive, Solution().longestConsecutive_clumsy], [root])
