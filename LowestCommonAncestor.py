from test_script import TreeNode, TreeUtil


class Solution:
    def getChild2ParentMap(self, root: TreeNode):
        child2parent = {root: None}
        for node in TreeUtil.preOrderTraversalIterator(root):
            if node.left:
                child2parent[node.left] = node
            if node.right:
                child2parent[node.right] = node
        return child2parent

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def getAncestors(node: TreeNode):
            ancestors = []
            while node is not None:
                ancestors.append(node)
                node = child2parent[node]
            return ancestors

        child2parent = self.getChild2ParentMap(root)
        ancestorsP = getAncestors(p)
        ancestorsQ = getAncestors(q)
        for pAncestorNode in ancestorsP:
            if pAncestorNode in ancestorsQ:
                return pAncestorNode
        return root


class Solution2:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def contain(root: TreeNode, findNode: TreeNode):
            return TreeUtil.findNodeByVal(root, findNode.val)
        def getCommonAncestor(node: TreeNode):
            if node is p:
                if contain(node, q):
                    return node
                return None
            elif node is q:
                if contain(node, p):
                    return node
                return None
            if contain(node.left, p):
                if contain(node.right, q):
                    return node
                return getCommonAncestor(node.left)
            elif contain(node.left, q):
                if contain(node.right, p):
                    return node
                return getCommonAncestor(node.right)

        return getCommonAncestor(root)


# root = TreeUtil.createBinaryTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
root = TreeUtil.createBinaryTree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
print(Solution().lowestCommonAncestor(root, TreeUtil.findNodeByVal(root, 5), TreeUtil.findNodeByVal(root, 4)).val)
