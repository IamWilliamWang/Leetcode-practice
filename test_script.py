from typing import List, Tuple, Iterator
import time
from math import log2
import bisect
from functools import wraps
from itertools import islice


# region 实用函数
class Wrappers:
    @staticmethod
    def timer(function):
        """
        输出该函数的运行时长
        :param function: 函数
        :return:
        """

        @wraps(function)  # 将此函数伪装成function
        def decorator(*args, **kwargs):
            startTime = time.time()
            ans = function(*args, **kwargs)
            endTime = time.time()
            print('{} 运行用时：{} s'.format(function.__name__, endTime - startTime))
            return ans

        return decorator

    @staticmethod
    def deprecated(newFunctionName=''):
        """
        弃用该函数，输出弃用警告
        :param newFunctionName: 新函数名称
        :return: 装饰器的实体
        """

        def deprecatedWrapper(function):
            """
            装饰器实体，用于接受@下面的函数
            :param function: 要弃用的函数
            :return: 经过弃用装饰后的原函数
            """

            @wraps(function)
            def showDeprecatedInfo(*args, **kwargs):
                import warnings
                if not newFunctionName:
                    warnings.warn("The '{}' function is deprecated".format(function.__name__), DeprecationWarning, 2)
                else:
                    warnings.warn(
                        "The '{}' function is deprecated, use '{}' instead".format(function.__name__, newFunctionName),
                        DeprecationWarning, 2)
                return function(*args, **kwargs)

            return showDeprecatedInfo

        return deprecatedWrapper


timer = Wrappers.timer
deprecated = Wrappers.deprecated()


def speedtest(functions: tuple, arguments: tuple) -> None:
    """
    对相似函数（参数类型都相同）统一进行速度测试，并输出结果
    :param functions: 包含所有函数的tuple
    :param arguments: 包含所有调用参数的tuple
    :return:
    """
    if not functions:
        return
    results = []  # 保存运行结果
    runtimes = []  # 保存运行时间
    columnsize = [0, 0, 0]  # 保存表格的每一列宽
    # 开始调用
    for function in functions:
        # 进行调用，记录结果和运行时间
        start = time.time()
        results.append(function(*arguments))
        runtimes.append(time.time() - start)
        # 调整每一列的宽度，不要让某一列的输出越界
        columnsize[0] = max(columnsize[0], len(function.__name__))
        columnsize[1] = max(columnsize[1], len(str(results[-1])))
        columnsize[2] = max(columnsize[2], len(str(runtimes[-1])))
    # 开始输出表格
    c_style_format = ('%-{}s|%-{}s|%-{}s'.format(*columnsize))  # C风格。实现了表格的左对齐
    print(c_style_format % ('Function', 'Return', 'Time'))  # 输出表头
    for i in range(len(results)):  # 输出函数，返回值，执行时间
        print((c_style_format + ' s') % (functions[i].__name__, results[i], runtimes[i]))
    # 输出执行时间比
    compareTimesStr = '执行时间比：'
    runtimesMin = min(runtimes)
    for runtime in runtimes:
        compareTimesStr += str(runtime / runtimesMin) + ': '
    print(compareTimesStr[:-2])


# endregion

# region 数据结构的节点定义
class ListNode:
    """
    Definition for singly-linked list.
    """

    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return str(ListUtil.traverse(self, False))


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        return TreeUtil.toString(self)


# endregion

# region 数据结构的帮助函数
class ListUtil:
    @staticmethod
    def createListWithHead(valList: List[object]) -> ListNode:
        """
        创建带有头节点的单向链表。头节点存储链表长度
        :param valList:
        :return:
        """
        head = ListNode(len(valList))
        previous = head
        for val in valList:
            node = ListNode(val)
            previous.next = node
            previous = previous.next
        return head

    @staticmethod
    def iterator(headNode: ListNode) -> Iterator[ListNode]:
        """
        链表的迭代器
        :param headNode: 头节点
        :return:
        """
        while headNode is not None:
            nextNode = headNode.next  # 保证无论该节点发生什么都能按照原先的顺序进行遍历
            yield headNode
            headNode = nextNode

    @staticmethod
    def traverse(headNode: ListNode, printWhileTraverse=True) -> List[object]:
        """
        遍历无头部的单向链表，返回遍历的结果
        :param headNode: 无头链表的第一个节点
        :param printWhileTraverse: 是否遍历时输出
        :return:
        """
        valList = [node.val for node in list(ListUtil.iterator(headNode))]
        for val in valList:
            if printWhileTraverse:
                print(val, end=' ')
        if printWhileTraverse:
            print()
        return valList


class TreeUtil:
    @staticmethod
    def createTreeByHeap(numberList: List[object]) -> TreeNode:
        """
        根据heap创建二叉树，返回根部节点
        :param numberList: 储存数据的heap
        :return:
        """
        nodeHeap = [TreeNode(x) if x is not None else None for x in numberList]  # 把heap转换成TreeNode heap
        for i in range(len(nodeHeap)):  # heap的大小不确定，所以要遍历每个node
            if nodeHeap[i] is None:  # 不要处理空节点
                continue
            if (i + 1) * 2 - 1 < len(nodeHeap):  # 连接每个元素的左子树
                nodeHeap[i].left = nodeHeap[(i + 1) * 2 - 1]
            if (i + 1) * 2 < len(nodeHeap):  # 连接每个元素的右子树
                nodeHeap[i].right = nodeHeap[(i + 1) * 2]
        return nodeHeap[0] if nodeHeap else None

    @Wrappers.deprecated('createTreeByHeap')
    def createBinaryTree(*args, **kwargs):  # 向后兼容API
        return TreeUtil.createTreeByHeap(*args, **kwargs)

    @staticmethod
    def createTreeByPreInOrder(preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        利用树的先序遍历和中序遍历结果来创建对应的二叉树
        :param preorder: 先序遍历结果
        :param inorder: 中序遍历结果
        :return:
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        inorderRootIndex = inorder.index(preorder[0])
        inorderLeftTree = inorder[:inorderRootIndex]
        if inorderRootIndex > 0:
            root.left = TreeUtil.createTreeByPreInOrder(preorder[1:1 + len(inorderLeftTree)], inorderLeftTree)
        inorderRightTree = inorder[inorderRootIndex + 1:]
        if 1 + len(inorderLeftTree) < len(preorder):
            root.right = TreeUtil.createTreeByPreInOrder(preorder[1 + len(inorderLeftTree):], inorderRightTree)
        return root

    @staticmethod
    def preOrderTraversal(rootNode: TreeNode) -> List[object]:
        """
        先序遍历，返回遍历结果
        :param rootNode: 根节点
        :return:
        """
        return [node.val for node in list(TreeUtil.preOrderTraversalIterator(rootNode))]

    @staticmethod
    def preOrderTraversalIterator(rootNode: TreeNode) -> Iterator[TreeNode]:
        """
        先序遍历，返回指向节点的迭代器
        :param rootNode: 根节点
        :return:
        """
        if rootNode is not None:
            yield rootNode
            yield from TreeUtil.preOrderTraversalIterator(rootNode.left)
            yield from TreeUtil.preOrderTraversalIterator(rootNode.right)

    @staticmethod
    def inOrderTraversal(rootNode: TreeNode) -> List[object]:
        """
        中序遍历，返回遍历结果
        :param rootNode: 根节点
        :return:
        """
        return [node.val for node in list(TreeUtil.inOrderTraversalIterator(rootNode))]

    @staticmethod
    def inOrderTraversalIterator(rootNode: TreeNode) -> Iterator[TreeNode]:
        """
        中序遍历，返回指向节点的迭代器
        :param rootNode: 根节点
        :return:
        """
        stack = []
        nowNode = rootNode
        # 先一直找到最最左下角
        while nowNode is not None:
            stack.append(nowNode)  # 访问节点
            nowNode = nowNode.left
        # 栈不为空时循环
        while stack:
            node = stack.pop()  # 取当前节点，访问
            yield node
            if node.right:  # 如果右节点存在，把右节点、右的左节点、右的左左节点等等入栈
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left

    @staticmethod
    def postOrderTraversal(rootNode: TreeNode) -> List[object]:
        """
        后序遍历，返回遍历结果
        :param rootNode: 根节点
        :return:
        """
        return [node.val for node in list(TreeUtil.postOrderTraversalIterator(rootNode))]

    @staticmethod
    def postOrderTraversalIterator(rootNode: TreeNode) -> Iterator[TreeNode]:
        """
        后序遍历，返回指向节点的迭代器
        :param rootNode: 根节点
        :return:
        """
        if rootNode is not None:
            yield from TreeUtil.preOrderTraversalIterator(rootNode.left)
            yield from TreeUtil.preOrderTraversalIterator(rootNode.right)
            yield rootNode

    @staticmethod
    def breadthFirstTraversal(rootNode: TreeNode) -> List[List[object]]:
        """
        广度优先遍历，返回二维数组，一维是每层的元素List，二维是第几层
        :param rootNode: 根节点
        :return:
        """
        resultList = []
        if rootNode is None:
            return resultList
        queue = [(rootNode, 1)]  # 装有(元素, 层号)的队列
        while queue:
            node, level = queue.pop(0)
            if level > len(resultList):  # result中没有存过该level的元素
                resultList.append([node.val])
            else:
                resultList[level - 1].append(node.val)
            # 左右节点入队列
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        return resultList

    @staticmethod
    def findNodeByVal(rootNode: TreeNode, val: object):
        """
        根据val寻找节点，如果没找到就返回None
        :param rootNode: 根节点
        :param val: 要找的节点储存的val
        :return:
        """
        for node in TreeUtil.preOrderTraversalIterator(rootNode):
            if node.val == val:
                return node
        return None

    _maxLevelCache = {}

    @staticmethod
    def maxLevel(rootNode: TreeNode, cacheEnabled=False) -> int:
        """
        计算二叉树的最大层数
        :param rootNode: 根节点
        :param cacheEnabled: 是否使用和储存本树根的最大层数
        :return:
        """
        if not rootNode:
            return 0
        if cacheEnabled:
            if rootNode not in TreeUtil._maxLevelCache:  # 不用lru_cache是因为树有可能会变化，会影响到第二次调用
                TreeUtil._maxLevelCache[rootNode] = len(TreeUtil.breadthFirstTraversal(rootNode))
            return TreeUtil._maxLevelCache[rootNode]
        return len(TreeUtil.breadthFirstTraversal(rootNode))

    @staticmethod
    def toValHeap(rootNode: TreeNode) -> List[object]:
        """
        将根节点代表的树转换成存储各个节点的val的堆
        :param rootNode: 根节点
        :return:
        """
        maxLevel = TreeUtil.maxLevel(rootNode, cacheEnabled=True)  # 计算最大层数
        valList = [None] * (2 ** maxLevel - 1)  # 按照元素可能的最大个数，初始化变量列表
        queue = [(rootNode, 0)]  # 储存(节点, 索引号)的队列
        # 队列不为空时循环（这里为了直观所以用的是广度优先）
        while queue:
            node, index = queue.pop(0)  # 取出节点和索引号
            valList[index] = node.val  # 访问节点，储存val
            # 左右节点和其对应的索引号入队列
            if node.left:
                queue.append((node.left, (index + 1) * 2 - 1))
            if node.right:
                queue.append((node.right, (index + 1) * 2))
        return valList

    @staticmethod
    def toString(rootNode: TreeNode, noneReplacer='X') -> str:
        """
        将二叉树转换为字符串，空缺的位置用'X'代替
        :param rootNode: 根节点
        :param noneReplacer: 如果遍历到空缺的节点，用什么代替
        :return:
        """
        if not rootNode:  # 根节点是空的
            return ''

        valList = TreeUtil.toValHeap(rootNode)  # 将树内的每个节点转成val堆
        string = ''
        for i in range(len(valList)):
            if valList[i] is not None:
                string += str(valList[i]) + ' '
            else:  # 将X代替None，可以很直观的输出
                string += noneReplacer + ' '
            if log2(i + 2) == int(log2(i + 2)):  # 符合这个条件的都是每层的最后一个元素
                string += '\n'
        # 进行全部对其操作
        lines = string.strip().split('\n')
        for i in range(len(lines) - 1):  # 最后一行不用添加空格
            lines[i] = ' ' * ((len(lines[-1]) - len(lines[i])) // 2) + lines[i]  # 在每一行前面添加空格
        return '\n'.join(lines)


# endregion

# region 常用算法
class Prime:  # mao1112
    """
    获得素数数组的高级实现。支持 in 和 [] 运算符，[]支持切片
    """

    def __init__(self):
        self._n: int = 6  # 素数列表的长度
        self._list: List[int] = [2, 3, 5, 7, 11, 13]  # 保存所有现有的素数列表

    def __contains__(self, n: int) -> bool:
        """
        判断n是否是素数
        :param n: 要判断的素数
        :return: 是否是素数
        """
        if not n % 2:  # 偶数只有2是素数
            return n == 2
        a, b = self.indexOf(n)  # 搜索n在素数列表中的位置
        return a == b  # 如果a b相同，代表这就是n在素数列表中的位置

    def __getitem__(self, i):
        """
        i为正整数时返回第i个元素；i为slice时返回切片数组（当i.stop=None时只返回迭代器）
        :param i: index或者slice
        :return: int或list或iterator
        """
        if isinstance(i, slice):  # 如果i是切片
            it = self.range(i.start, i.stop, i.step)  # 获得迭代器
            if i.stop:  # 如果指定了stop，则返回对应的数组
                return list(it)
            return it  # 没指定就直接返回迭代器
        else:  # 如果n是正整数
            self._extendToLen(i + 1)  # 拓展list长度直到n
            return self._list[i]  # 返回第n个元素

    def indexOf(self, n: int) -> Tuple[int, int]:
        """
        获得数字n位于素数列表的第几个位置，或者哪两个位置之间
        :param n: 要搜索的素数
        :return: 如果搜到则返回(index, index)；搜不到则返回n的大小在哪两个相邻位置之间(from, to)
        """
        if n < 2:
            return -1, 0
        if n > self._list[-1]:  # 需要拓展列表
            self._extend(n)
        index = bisect.bisect(self._list, n)  # 二分法搜索大于n的最左边位置
        if self._list[index - 1] == n:
            return index - 1, index - 1
        else:
            return index - 1, index

    def range(self, start=0, stop=None, step=1) -> islice:
        """
        获得素数数组的range迭代器
        :return: 迭代器
        """
        if stop:  # 如果有指明stop的话
            self._extendToLen(stop + 1)  # 拓宽list到stop位置
            return islice(self._list, start, stop, step)  # 生成切片后的迭代器
        return islice(self, start, None, step)  # 只有没指定stop时制造迭代器的切片，返回指向n.start位置的迭代器

    def primeRange(self, minN: int, maxN: int, step=1) -> Iterator:
        """
        返回包含[minN, maxN)内所有素数的迭代器
        :param minN: 素数最小值
        :param maxN: 素数最大值（不包括）
        :param step: 遍历的步伐，默认为1
        :return: 迭代器
        """
        minN = max(2, minN)  # 开始值合法化
        if minN >= maxN:  # 异常参数检查
            return
        self._extend(maxN)  # 拓展list直到包含stop
        i = self.indexOf(minN)[1]  # 找到startN所在的位置，或者startN可以插入的位置
        beginning_i = i
        while i < len(self._list):  # 防止数组越界（其实不会，因为extend过了，一定是break之前就return）
            p = self._list[i]  # 获取第i个元素
            if p < maxN:  # 每次必须小于maxN才能yield
                if (i - beginning_i) % step == 0:
                    yield p
                i += 1
            else:  # 超过范围就跳出
                return

    def _extend(self, n: int) -> None:
        """
        拓展素数列表直到涵盖范围包括数字n就立刻停止
        :param n: 将素数列表拓展到哪个数字为止
        :return:
        """
        if n <= self._list[-1]:  # 如果list已经包含，则不需要拓展
            return
        maxSqrt = int(n ** 0.5) + 1  # 要拓展到的位置
        self._extend(maxSqrt)  # 如果列表没有拓展到sqrt(n)，递归拓展
        begin = self._list[-1] + 1  # 从哪里开始搜索
        sizer = [i for i in range(begin, n + 1)]  # 生成所有数字的数组
        for prime in self.primeRange(2, maxSqrt):  # 得到[2,maxSqrt)所有的素数
            for i in range(-begin % prime, len(sizer), prime):
                sizer[i] = 0  # 把所有非素数变为0
        self._list += [x for x in sizer if x]  # 删去所有的零，剩下的就是素数列表

    def _extendToLen(self, listLen: int) -> None:
        """
        将素数列表的长度至少拓展到listLen
        :param listLen: 至少拓展到多长
        :return:
        """
        while len(self._list) < listLen:  # 每次n*1.5，直到list长度符合要求
            self._extend(int(self._list[-1] * 1.5))


class BisectUtil:
    @staticmethod
    def indexOf(collection: list, x) -> int:
        """
        在collection中搜索x出现的最左边的位置，没找到则返回-1
        :param collection: 数组
        :param x:
        :return:
        """
        i = bisect.bisect_left(collection, x)
        if i != len(collection) and collection[i] == x:
            return i
        return -1

    @staticmethod
    def find_lt(collection: list, x):
        """
        返回collection中max(小于x的数字)。如果没找到任何数字则产生ValueError
        :param collection: 数组
        :param x:
        :return:
        """
        i = bisect.bisect_left(collection, x)
        if i:
            return collection[i - 1]
        raise ValueError

    @staticmethod
    def find_le(collection: list, x):
        """
        返回collection中max(小于等于x的数字)。如果没找到任何数字则产生ValueError
        :param collection: 数组
        :param x:
        :return:
        """
        i = bisect.bisect_right(collection, x)
        if i:
            return collection[i - 1]
        raise ValueError

    @staticmethod
    def find_gt(collection: list, x):
        """
        返回collection中min(大于x的数字)。如果没找到任何数字则产生ValueError
        :param collection: 数组
        :param x:
        :return:
        """
        i = bisect.bisect_right(collection, x)
        if i != len(collection):
            return collection[i]
        raise ValueError

    @staticmethod
    def find_ge(collection: list, x):
        """
        返回collection中min(大于等于x的数字)。如果没找到任何数字则产生ValueError
        :param collection: 数组
        :param x:
        :return:
        """
        i = bisect.bisect_left(collection, x)
        if i != len(collection):
            return collection[i]
        raise ValueError


def binary_search(nums: List[object], target: object, mode=0, key=None, reverse=False):  # 提示：完美版本，请勿修改
    """
    二分查找法，返回target出现的位置，找不到返回-1。也可以搜索左边界(首次出现的位置)和右边界(最后出现的位置)，找不到返回-1
    :param nums: 整形或者object数组（默认为升序）
    :param target: 要查找的数字或者object（如果是数组里的是object而target是其里面的变量则需要传入key；如果数组和target是同一个类则需要实现该类的__lt__, __gt__和__eq__）
    :param mode: 0为二分查找，1为左边界搜索，2为右边界搜索
    :param key: 搜索时用什么值进行比较
    :param reverse: nums数组是否为降序
    :link: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/
    :return:
    """
    if key is None:  # 如果没指定，那么生成默认的key函数
        key = lambda element: element
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if (not reverse and key(nums[mid]) < target) or (reverse and key(nums[mid]) > target):
            left = mid + 1
        elif (not reverse and key(nums[mid]) > target) or (reverse and key(nums[mid]) < target):
            right = mid - 1
        elif key(nums[mid]) == target:
            if mode == 1:
                right = mid - 1  # 收缩左侧边界
            elif mode == 2:
                left = mid + 1  # 收缩左侧边界
            else:  # mode==0
                return mid  # 直接返回
        else:
            raise ValueError(
                'The search was accidentally terminated. Check whether the key function returns the specified output')
    if mode == 1:
        # 最后要检查 left 越界的情况
        if left >= len(nums) or nums[left] != target:
            return -1
        return left
    elif mode == 2:
        # 最后要检查 right 越界的情况
        if right < 0 or nums[right] != target:
            return -1
        return right
    else:  # mode==0
        return -1


# endregion

if __name__ == '__main__':
    # root = TreeUtil.createBinaryTree([-5, -1, -4, None, None, -5, 0, None, None, None, None, -5, None, -1, 2])
    # root.right.right.left.right = TreeUtil.createBinaryTree([-3, None, -5, None, None, None, -4])
    root = TreeUtil.createTreeByPreInOrder(preorder=[-5, -1, -4, -5, -5, 0, -1, -3, -5, -4, 2],
                                           inorder=[-1, -5, -5, -5, -4, -1, -3, -5, -4, 0, 2])
    print(root)

'''数据结构图
DataStructure = {'Collections': {'Map': [('dict', 'OrderDict', 'defaultdict'),
                                         ('chainmap', 'types.MappingProxyType')],
                                 'Set': [('set', 'frozenset'), {'multiset': 'collection.Counter'}]},
                 'Sequence': {'Basic': ['list', 'tuple', 'iterator']},
                 'Algorithm': {'Priority': ['heapq',
                                            'queue.PriorityQueue'],
                               'Queue': ['queue.Queue',
                                         'multiprocessing.Queue'],
                               'Stack': ['collection.deque',
                                         'queue.LifeQueue']},
                 'text_sequence': ['str', 'byte', 'bytearray']}
'''
