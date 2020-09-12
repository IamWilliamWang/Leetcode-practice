from collections import defaultdict
from test_script import TreeNode, TreeUtil


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        adjust = defaultdict(list)
        for node in TreeUtil.preOrderTraversalIterator(root):
            if node.left:
                adjust[node].append(node.left)
                adjust[node.left].append(node)
            if node.right:
                adjust[node].append(node.right)
                adjust[node.right].append(node)
        ans = 0
        for bfsRootNode in adjust:
            if bfsRootNode.left or bfsRootNode.right:
                continue
            queue = [(bfsRootNode, 0)]  # Node, _distance
            visited = set()
            while queue:
                node, _distance = queue.pop(0)
                if node in visited or _distance >= distance:
                    continue
                visited.add(node)
                for nextNode in filter(lambda node: node not in visited, adjust[node]):
                    if nextNode.left is None and nextNode.right is None:
                        if _distance < distance:
                            # print(bfsRootNode.val, nextNode.val)
                            ans += 1
                    else:
                        queue.append((nextNode, _distance + 1))
        return ans // 2


print(Solution().countPairs(TreeUtil.createTreeByHeap([1, 2, 3, None, 4, None, None]), 3))
print(Solution().countPairs(TreeUtil.createTreeByHeap([1, 2, 3, 4, 5, 6, 7]), 3))
