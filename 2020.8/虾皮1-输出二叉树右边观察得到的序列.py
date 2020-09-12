from test_script import TreeNode


def getRightSideVals(root: TreeNode):
    def BFS(node: TreeNode):
        nonlocal result
        queue = [(node, 1)]
        while queue:
            node, level = queue.pop(0)
            if node.left:
                queue += [(node.left, level + 1)]
            if node.right:
                queue += [(node.right, level + 1)]
            if not queue:  # BFS到最后一个节点
                result.append(node.val)
            else:
                if queue[0][1] > level:  # 现在是这一层的最后节点
                    result.append(node.val)

    result = []
    BFS(root)
    return result