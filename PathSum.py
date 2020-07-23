from typing import List

from test_script import TreeNode, TreeUtil


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if not root:  # 如果节点为空
            return []  # 返回null
        if sum == root.val and not root.left and not root.right:  # 如果sum - root.val == 0，证明找到了
            return [[root.val]]  # 返回1x1的矩阵
        retList = []  # 保存从左子树返回的二维矩阵
        leftRet = self.pathSum(root.left, sum - root.val)  # 减去当前节点的val
        if leftRet:  # 如果不是空，则表明左子树有所寻结果
            for valList in leftRet:  # 二维矩阵的左边加一列，这一列数字为val
                valList.insert(0, root.val)
            retList += leftRet  # 把他加进来
        rightRet = self.pathSum(root.right, sum - root.val)
        if rightRet:
            for valList in rightRet:
                valList.insert(0, root.val)
            retList += rightRet
        return retList  # 返回最终结果


print(Solution().pathSum(TreeUtil.createTreeByHeap([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, None, 5, 1]), 22))
print(Solution().pathSum(TreeUtil.createTreeByHeap([-2,-3,None]), -5))