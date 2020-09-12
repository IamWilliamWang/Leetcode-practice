from typing import Tuple

from test_script import TreeNode, TreeUtil


def balance(root: TreeNode) -> bool:
    def depth(node: TreeNode) -> Tuple[int, bool]:
        if not node:
            return 0, True
        left, vaild = depth(node.left)
        right, vaild = depth(node.right)
        if abs(left - right) > 1:
            return max(left, right) + 1, False
        else:
            return max(left, right) + 1, True

    _, ans = depth(root)
    return ans


"""
/*
 1.实现一个函数，检查二叉树是否平衡。平衡二叉树的定义如下：任意一个节点的左右子树高度差不超过1。假设二叉树节点一共有N个节点，要求算法时间复杂度不超过O(N)。
*/
// write your code here
   
/*
 2.实现两个大数的除法，输入为两个长数字字符串，结果精确到小数点后n位（n由输入参数决定）
/*
// write your code here

/*
 3.实现一个实数的堆栈，使得其 push pop max 方法的时间复杂度为 O(1)
*/
// write your code here

/*
 4.有一个整数二维数组，每行的元素个数不同，输出它的全排列，同一行的元素互斥。要求不使用递归完成
例：
输入：[A,B,C][D,E][F,G]
输出：ADF,ADG,AEF,AEG,BDF,BDG,BEF,BEG,CDF,CDG,CEF,CEG
*/
// write your code here

/*
 5.判断二维一个圆和一个OBB（轴向包围盒）是否相交
    public struct Point
    {
        public float x;
        public float y;
    }
    public struct Circle
    {
        public Point center;
        public float radius;
    }
    public struct OBB
    {
        public Point center;
        public float width;
        public float height;
        public float angleInRadian; // 用弧度表示 0-2PI
    }
*/
// write your code here
"""
