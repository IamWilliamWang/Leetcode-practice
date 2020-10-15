import bisect
import re
import sys
import time
from functools import wraps, singledispatch
from heapq import heappop, heappush
from itertools import islice
from math import log2
from typing import Iterator, Dict, List, Tuple

import numpy as np

sys.setrecursionlimit(10000)


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


@singledispatch
def shuffle(iterable) -> None:
    raise ValueError('Type ' + re.findall("'.+?'", str(type(iterable)))[0] + ' is not supported.')


@shuffle.register(list)
def _(_list) -> list:
    np.random.shuffle(_list)
    return _list


@shuffle.register(tuple)
def _(_tuple) -> tuple:
    _tuple = list(_tuple)
    np.random.shuffle(_tuple)
    return tuple(_tuple)


@shuffle.register(str)
def _(_str) -> str:
    charArray = [ch for ch in _str]
    np.random.shuffle(charArray)
    return ''.join(charArray)


def _printComparison(results, runtimes: list, ignoreOrder=True):
    # 输出一致性
    print('All equals: ', end='')
    if all((sorted(result) == sorted(results[0])) if type(result) == list and ignoreOrder and None not in result else (
            result == results[0]) for result in results):  # 如果是list则sort后再比较
        print('True')
    else:
        print('\033[1;31mFalse\033[0m')
    # 输出执行时间比
    compareTimesStr = 'Execution time ratio: '
    runtimesMin = min(runtimes)
    if runtimesMin == 0.0:
        return
    for runtime in runtimes:
        compareTimesStr += (str(runtime / runtimesMin) if runtime != runtimesMin else '1') + ': '
    print(compareTimesStr[:-2])


_speedtest_counter = 1


def speedtest_format(functions, arguments, ignoreOrder=True) -> None:
    """
    对相似函数（参数类型都相同）统一进行速度测试，并输出结果
    :param functions: 包含所有函数的tuple或者list
    :param arguments: 包含所有调用参数的tuple或者list
    :param ignoreOrder: 对结果list的顺序是否忽略
    :return:
    """
    if not functions:
        return
    global _speedtest_counter
    print('----- speedtest round %d -----' % _speedtest_counter)
    _speedtest_counter += 1
    results = []  # 保存运行结果
    runtimes = []  # 保存运行时间
    columnsize = [8, 6, 4]  # 保存表格的每一列宽
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
    _printComparison(results, runtimes, ignoreOrder)


def speedtest_realtime(functions, arguments, ignoreOrder=True) -> None:
    """
    对相似函数（参数类型都相同）统一进行速度测试，并实时的输出结果，但表格不一定对齐
    :param functions: 包含所有函数的tuple或者list
    :param arguments: 包含所有调用参数的tuple或者list
    :param ignoreOrder: 对结果list的顺序是否忽略
    :return:
    """
    if not functions:
        return
    global _speedtest_counter
    print('----- speedtest round %d -----' % _speedtest_counter)
    _speedtest_counter += 1
    results = []  # 保存运行结果
    runtimes = []  # 保存运行时间
    columnsize = [8, 6, 4]  # 保存表格的每一列宽
    for function in functions:
        columnsize[0] = max(columnsize[0], len(function.__name__))
    # 开始输出表格
    c_style_format = ('%-{}s|%-{}s|%-{}s'.format(*columnsize))  # C风格。实现了表格的左对齐
    print(c_style_format % ('Function', 'Return', 'Time'))  # 输出表头
    # 开始调用
    for i, function in enumerate(functions):
        print(c_style_format.split('|')[0] % function.__name__, end='|')
        # 进行调用，记录结果和运行时间
        start = time.time()
        results.append(function(*arguments))
        runtimes.append(time.time() - start)
        if len(str(results[i])) > columnsize[1]:
            columnsize[1] = len(str(results[i]))
            c_style_format = ('%-{}s|%-{}s|%-{}s'.format(*columnsize))
        print((c_style_format[c_style_format.find('|') + 1:] % (results[i], runtimes[i])).strip(), end=' s\n')
    _printComparison(results, runtimes, ignoreOrder)


speedtest = speedtest_realtime


def standard(function, retValueStandard):
    """
    生成speedtest基准函数
    :param function: 你的函数
    :param retValueStandard: 应该返回的值
    :return: tuple(你的函数, 基准函数)
    """

    def truth(*args):
        return retValueStandard

    return function, truth


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
        return str(ListUtil.traverse(self))


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
    def createList(valList: list) -> ListNode:
        """
        创建无头节点的单向链表
        :param valList:
        :return:
        """
        return ListUtil.createListWithHead(valList).next

    @staticmethod
    def createListWithHead(valList: list):
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
        :param headNode 头节点
        :return:
        """
        nodeList = []
        while headNode:
            nodeList.append(headNode)
            headNode = headNode.next
        # 遍历时支持修改
        return (node for node in nodeList)

    @staticmethod
    def traverse(headNode: ListNode) -> list:
        """
        遍历无头部的单向链表，返回遍历的结果
        :param headNode 无头链表的第一个节点
        :return:
        """
        return [node.val for node in list(ListUtil.iterator(headNode))]


class TreeUtil:
    @staticmethod
    def createTreeByHeap(numberList: list) -> TreeNode:
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

    @staticmethod
    def createTreeByHeapExpressedByDict(numberDict: Dict[int, object]) -> TreeNode:
        """
        根据使用dict表达的heap创建二叉树，返回根部节点
        :param numberDict: 储存数据的heap对应的dict（index: val）
        :return:
        """
        nodeHeapDict = {index: TreeNode(numberDict[index]) for index in numberDict}  # 把index: val变成index: TreeNode(val)
        for i in nodeHeapDict:
            if ((i + 1) * 2 - 1) in nodeHeapDict:  # 连接每个元素的左子树
                nodeHeapDict[i].left = nodeHeapDict[(i + 1) * 2 - 1]
            if ((i + 1) * 2) in nodeHeapDict:  # 连接每个元素的右子树
                nodeHeapDict[i].right = nodeHeapDict[(i + 1) * 2]
        return nodeHeapDict[0] if 0 in nodeHeapDict else None

    @staticmethod
    def serialize(root: TreeNode) -> str:
        """
        序列化一棵树，返回转换好的str
        :param root:
        :return:
        """
        if not root:
            return "[]"
        queue = [root]
        result = []
        while queue:
            node = queue.pop(0)
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append('None')
        return '[' + ', '.join(map(str, result)) + ']'

    @staticmethod
    def deserialize(serializedStr: str) -> TreeNode:
        """
        反序列化一棵树，将str转换成树，返回根节点
        :param serializedStr:
        :return:
        """
        if serializedStr == "[]":
            return None
        vals, i = serializedStr[1:-1].split(','), 1
        root = TreeNode(int(vals[0]))
        queue = [root]
        while queue:
            node = queue.pop(0)
            if vals[i] != 'None':
                node.left = TreeNode(int(vals[i]))
                queue.append(node.left)
            i += 1
            if vals[i] != 'None':
                node.right = TreeNode(int(vals[i]))
                queue.append(node.right)
            i += 1
        return root

    @Wrappers.deprecated('createTreeByHeap')
    def createBinaryTree(*args, **kwargs):  # 向后兼容API
        return TreeUtil.createTreeByHeap(*args, **kwargs)

    @staticmethod
    def createTreeByPreInOrder(preorder, inorder) -> TreeNode:
        """
        利用树的先序遍历和中序遍历结果来创建对应的二叉树
        :param preorder: List[int]或str 先序遍历结果
        :param inorder: List[int]或str 中序遍历结果
        :return:
        """
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        inOrderRootIndex = inorder.index(preorder[0])
        inOrderLeft = inorder[:inOrderRootIndex]
        inOrderRight = inorder[inOrderRootIndex + 1:]
        preOrderLeft = preorder[1:1 + len(inOrderLeft)]
        preOrderRight = preorder[1 + len(inOrderLeft):]
        root.left = TreeUtil.createTreeByPreInOrder(preOrderLeft, inOrderLeft)
        root.right = TreeUtil.createTreeByPreInOrder(preOrderRight, inOrderRight)
        return root

    @staticmethod
    def createTreeByInPostOrder(inorder, postorder) -> TreeNode:
        """
        利用树的中序遍历和后序遍历结果来创建对应的二叉树
        :param inorder: List[int]或str 中序遍历结果
        :param postorder: List[int]或str 后序遍历结果
        :return:
        """
        if len(inorder) != len(postorder) or not inorder or not postorder:
            return None
        root = TreeNode(postorder[-1])
        inOrderRootIdx = inorder.index(postorder[-1])
        inOrderLeft = inorder[:inOrderRootIdx]
        inOrderRight = inorder[inOrderRootIdx + 1:]
        postOrderLeft = postorder[:-1 - len(inOrderRight)]
        postOrderRight = postorder[-1 - len(inOrderRight):-1]
        root.left = TreeUtil.createTreeByInPostOrder(inOrderLeft, postOrderLeft)
        root.right = TreeUtil.createTreeByInPostOrder(inOrderRight, postOrderRight)
        return root

    @staticmethod
    def preOrderTraversal(rootNode: TreeNode) -> list:
        """
        先序遍历，返回遍历结果
        :param rootNode 根节点
        :return:
        """
        return [node.val for node in list(TreeUtil.preOrderTraversalIterator(rootNode))]

    @staticmethod
    def preOrderTraversalIterator(rootNode: TreeNode) -> Iterator[TreeNode]:
        """
        先序遍历，返回指向节点的迭代器
        :param rootNode 根节点
        :return:
        """
        if rootNode is not None:
            yield rootNode
            yield from TreeUtil.preOrderTraversalIterator(rootNode.left)
            yield from TreeUtil.preOrderTraversalIterator(rootNode.right)

    @staticmethod
    def inOrderTraversal(rootNode: TreeNode) -> list:
        """
        中序遍历，返回遍历结果
        :param rootNode 根节点
        :return:
        """
        return [node.val for node in list(TreeUtil.inOrderTraversalIterator(rootNode))]

    @staticmethod
    def inOrderTraversalIterator(rootNode: TreeNode) -> Iterator[TreeNode]:
        """
        中序遍历，返回指向节点的迭代器
        :param rootNode 根节点
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
    def postOrderTraversal(rootNode: TreeNode) -> list:
        """
        后序遍历，返回遍历结果
        :param rootNode 根节点
        :return:
        """
        return [node.val for node in list(TreeUtil.postOrderTraversalIterator(rootNode))]

    @staticmethod
    def postOrderTraversalIterator(rootNode: TreeNode) -> Iterator[TreeNode]:
        """
        后序遍历，返回指向节点的迭代器
        :param rootNode 根节点
        :return:
        """
        if rootNode is not None:
            yield from TreeUtil.postOrderTraversalIterator(rootNode.left)
            yield from TreeUtil.postOrderTraversalIterator(rootNode.right)
            yield rootNode

    @staticmethod
    def breadthFirstTraversal(rootNode: TreeNode) -> List[list]:
        """
        广度优先遍历，返回二维数组，一维是每层的元素List，二维是第几层
        :param rootNode 根节点
        :return:
        """
        return list(TreeUtil.breadthFirstTraversalIterator(rootNode))

    @staticmethod
    def breadthFirstTraversalIterator(rootNode: TreeNode) -> Iterator[list]:
        """
        广度优先遍历，每次返回一层的元素List
        :param rootNode 根节点
        :return:
        """
        resultList = []  # 保存每一层元素的二维数组
        if rootNode is None:
            return
        queue = [(rootNode, 1)]  # 装有(元素, 层号)的队列
        while queue:
            node, level = queue.pop(0)
            if level > len(resultList):  # result中没有存过该level的元素
                if resultList:
                    yield resultList[level - 2]
                resultList.append([node.val])
            else:
                resultList[level - 1].append(node.val)
            # 左右节点入队列
            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))
        yield resultList[-1]

    @staticmethod
    def findNodeByVal(rootNode: TreeNode, val) -> TreeNode:
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

    @staticmethod
    def maxLevel(rootNode: TreeNode) -> int:
        """
        计算二叉树的最大层数
        :param rootNode: 根节点
        :return:
        """
        if not rootNode:
            return 0
        return len(TreeUtil.breadthFirstTraversal(rootNode))

    maxDepth = maxLevel

    @staticmethod
    def toValHeap(rootNode: TreeNode) -> list:
        """
        将根节点代表的树转换成存储各个节点的val的堆
        :param rootNode: 根节点
        :return:
        """

        def assign(index: int, element):
            nonlocal valList
            if index >= len(valList):  # 拓展数组
                valList += [None] * (2 ** maxLevel - 1 - len(valList))
            valList[index] = element  # 访问节点，储存val

        if not rootNode:
            return []
        maxLevel = 1
        valList = [None] * (2 ** maxLevel - 1)  # 按照元素可能的最大个数，初始化变量列表
        queue = [(rootNode, 1, 0)]  # 储存(节点, 索引号)的队列
        # 队列不为空时循环（这里为了直观所以用的是广度优先）
        while queue:
            node, level, index = queue.pop(0)  # 取出节点和索引号
            maxLevel = max(maxLevel, level)
            assign(index, node.val)
            # 左右节点和其对应的索引号入队列
            if node.left:
                queue.append((node.left, level + 1, (index + 1) * 2 - 1))
            if node.right:
                queue.append((node.right, level + 1, (index + 1) * 2))
        return valList

    @staticmethod
    def toValHeapToDict(rootNode: TreeNode) -> Dict[int, object]:
        """
        将根节点代表的树转换成存储各个节点的val的堆，再把堆转换成dict（index: TreeNode）
        :param rootNode: 根节点
        :return:
        """
        if not rootNode:
            return {}
        maxLevel = 1
        valDict = {}
        queue = [(rootNode, 1, 0)]  # 储存(节点, 索引号)的队列
        # 队列不为空时循环（这里为了直观所以用的是广度优先）
        while queue:
            node, level, index = queue.pop(0)  # 取出节点和索引号
            maxLevel = max(maxLevel, level)
            valDict[index] = node.val
            # 左右节点和其对应的索引号入队列
            if node.left:
                queue.append((node.left, level + 1, (index + 1) * 2 - 1))
            if node.right:
                queue.append((node.right, level + 1, (index + 1) * 2))
        return valDict

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


class GraphUtil:
    @staticmethod
    def BFS(adjMap, start):
        """
        广度优先遍历
        :param adjMap: Dict[int, List[int]]或Dict[str, List[str]] 使用邻接表表达节点关系
        :param start: int或str 开始节点
        :return: Iterator[int]或Iterator[str] 每次返回遍历的节点号
        """
        queue = [start]
        visited = {start}
        while queue:
            node = queue.pop(0)
            for nextNode in adjMap[node]:
                if nextNode not in visited:
                    queue.append(nextNode)
                    visited.add(nextNode)
            yield node

    @staticmethod
    def DFS(adjMap, start, 升序优先=False):
        """
        深度优先遍历
        :param adjMap: Dict[int, List[int]]或Dict[str, List[str]] 使用邻接表表达节点关系
        :param start: int或str 开始节点
        :param 升序优先: 优先遍历数字较小的节点
        :return: Iterator[int]或Iterator[str] 每次返回遍历的节点号
        """
        stack = [start]
        visited = {start}
        while stack:
            node = stack.pop()
            if 升序优先:
                nextNodes = sorted(adjMap[node], reverse=True)  # 数值小的越靠近栈顶
            else:
                nextNodes = adjMap[node]
            for nextNode in nextNodes:
                if nextNode not in visited:
                    stack.append(nextNode)
                    visited.add(nextNode)
            yield node

    @staticmethod
    def createMatrix(edges, nodeCount=-1):
        """
        根据输入的[(from, to)]构建邻接矩阵，或者
        根据输入的[(from, to, distance)]构建邻接距离矩阵
        :param edges: List[tuple] from节点, to节点, 边长。节点一定要是从零开始的整数
        :param nodeCount: 节点数
        :return:
        """
        if nodeCount == -1:
            nodeCount = max(id for tpl in edges for id in tpl) + 1
        if len(edges[0]) == 2:
            matrix = [0 * nodeCount for _ in range(nodeCount)]
            for fromNode, toNode in edges:
                matrix[fromNode][toNode] = 1
            return matrix
        else:
            matrix = [[2 ** 31 - 1] * nodeCount for _ in range(nodeCount)]
            for i in range(nodeCount):
                matrix[i][i] = 0
            for fromNode, toNode, distance in edges:
                matrix[fromNode][toNode] = distance
            return matrix

    @staticmethod
    def createMatrixByAdjDict(adjDict):
        """
        将邻接表/邻接距离表转换成邻接矩阵/邻接距离矩阵
        :param adjDict: Dict[int, List[tuple]]
        :return:
        """
        allTuples = []
        for key in adjDict:
            allTuples += [tuple([key] + [x for x in tpl]) for tpl in adjDict[key]]
        return GraphUtil.createMatrix(allTuples, max(adjDict) + 1)

    @staticmethod
    def dijstra(matrix: List[List[int]], start: int):
        """
        :param matrix: 有向图的邻接矩阵，元素代表边的长度
        :param start: 根节点
        :return: 最短路径长度(不可达为-1)和最短路径(不可达为[])
        """
        assert matrix and len(matrix) == len(matrix[0])
        shortestDist = [0] * len(matrix)  # 最短路径的长度
        visited = [False] * len(matrix)  # 最短路径是否已求出
        path = [[start, i] for i in range(len(matrix))]  # 路径，并初始化
        shortestDist[start] = 0  # 初始化源节点
        visited[start] = True
        for i in range(1, len(matrix)):
            minNum = 2 ** 31 - 1
            index = -1
            for k in range(len(matrix)):
                # 已经求出的节点不需要再计算
                if not visited[k] and matrix[start][k] < minNum:
                    minNum = matrix[start][k]
                    index = k
            # 更新最短路径
            shortestDist[index] = minNum
            visited[index] = True
            # 更新从index跳到其它节点的较短路径
            for k in range(len(matrix)):
                if not visited[k] and matrix[start][index] + matrix[index][k] < matrix[start][k]:
                    matrix[start][k] = matrix[start][index] + matrix[index][k]
                    path[k] = path[index].copy() + [k]
        path[start].pop()
        for i in range(len(shortestDist)):
            if shortestDist[i] >= 2 ** 31 - 1:
                shortestDist[i] = -1
                path[i] = []
        return shortestDist, path

    @staticmethod
    def getCircles(matrix: List[List[int]], startNode: int):
        """
        获得所有环的路径
        :param matrix: 邻接矩阵
        :param startNode: 从哪个点开始DFS
        :return:
        """

        def findCycle(v):
            if v in trace:
                yield trace[trace.index(v):]
                return
            trace.append(v)
            for i in range(len(matrix)):
                if matrix[v][i] != 0:
                    yield from findCycle(i)
            trace.pop()

        trace = []
        yield from findCycle(startNode)

    @staticmethod
    def kruskal(graph: Dict[int, List[Tuple[int, int]]]):
        """
        根据邻接距离表生成最小生成树
        :param graph:
        :return:
        """
        N = len(graph)  # 得到图中点的个数
        mst, edges = [], []
        reps = list(range(N))  # 初始化代表元
        for vi in range(N):  # 收集各边
            for vj, weight in graph[vi]:
                edges.append((weight, vi, vj))
        edges.sort()  # 将边按权值weight从小到大排序
        for weight, vi, vj in edges:  # 逐个遍历边，将其加入到mst中
            if reps[vi] != reps[vj]:
                mst.append((vi, vj, weight))
                for v in range(N):  # 更新代表元
                    if reps[v] == reps[vj]:
                        reps[v] = reps[vi]
        return mst

    @staticmethod
    def prim(graph: Dict[int, List[Tuple[int, int]]]):
        """
        根据邻接距离表生成最小生成树
        :param graph:
        :return:
        """
        N = len(graph)
        edges = [(0, 0, 0)]  # 每次将新边加入到一个优先队列中
        mst = [None] * N  # 用于判断边所连接的点是否已经遍历过
        edge_count = 0
        while edge_count < N and edges:
            weight, vi, vj = heappop(edges)
            if not mst[vj]:
                edge_count += 1
                mst[vj] = (vi, weight)
                for i, w in graph[vj]:  # 将新点的出边加入优先队列
                    if not mst[i]:
                        heappush(edges, (w, vj, i))
        return mst


# endregion


class LoopQueue:
    """
    允许覆盖的循环队列
    """

    def __init__(self, maxsize=100):
        self._queue = [None] * (maxsize + 1)
        self._head = 0
        self._tail = 0
        self._maxsize = maxsize + 1

    def offer(self, element):
        self._queue[self._tail] = element
        self._tail += 1
        self._tail %= self._maxsize
        if self._tail == self._head:  # 队列满了，出队一次
            self._head = (self._head + 1) % self._maxsize

    def offerAll(self, constList: list):
        if len(constList) > self.capacity():
            constList = constList[-self.capacity():]
        i, j = -self._maxsize + self._tail, 0
        while j < len(constList):
            self._queue[i] = constList[j]
            self._tail = (self._tail + 1) % self._maxsize
            if self._tail == self._head:  # 队列满了，出队一次
                self._head = (self._head + 1) % self._maxsize
            i, j = i + 1, j + 1

    def poll(self):
        if self.size() < 1:
            raise ValueError
        ans = self._queue[self._head]
        self._head = (self._head + 1) % self._maxsize
        return ans

    def peek(self):
        if self.size() == 0:
            return None
        return self._queue[self._head]

    def size(self):
        return (self._tail - self._head) % self._maxsize

    def capacity(self):
        return self._maxsize - 1

    def copy(self):
        newQueue = LoopQueue(self._maxsize - 1)
        newQueue.offerAll(self.tolist())
        return newQueue

    def tolist(self):
        if self.size() == 0:
            return []
        if self._head < self._tail:
            return self._queue[self._head:self._tail]
        return self._queue[self._head:] + self._queue[:self._tail]

    def __bool__(self):
        return self.size() != 0

    def __copy__(self):
        return self.copy()

    def __eq__(self, other):
        if type(self) == type(other):
            return self.tolist() == other.tolist()
        return self.tolist() == other

    def __iter__(self):
        return iter(self.tolist())

    def __len__(self):
        return self.size()

    def __str__(self):
        return str(self.tolist())


# region 常用算法
class Prime:
    """
    生成素数的便捷类。支持 in 和 [] 运算符，其中[]支持切片
    """

    def __init__(self):
        self._list = [2, 3, 5, 7, 11, 13]  # 保存所有现有的素数列表

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

    def indexOf(self, n: int):
        """
        获得数字n位于素数列表的第几个位置，或者哪两个位置之间
        :param n: 要搜索的素数
        :return: Tuple[int, int] 如果搜到则返回(index, index)；搜不到则返回n的大小在哪两个相邻位置之间(from, to)
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

    def primeRange(self, minN: int, maxN: int, step=1):
        """
        返回包含[minN, maxN)内所有素数的迭代器
        :param minN: 素数最小值
        :param maxN: 素数最大值（不包括）
        :param step: 遍历的步伐，默认为1
        :return: Iterator 迭代器
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


def binary_search(nums, target: object, mode=0, key=None):
    """
    二分查找法，返回target出现的位置，找不到返回-1。也可以搜索左边界(首次出现的位置)和右边界(最后出现的位置)，找不到返回-1
    :param nums: List[object] 整形或者object数组（默认为升序）
    :param target: 要查找的数字或者object（如果是数组里的是object而target是其里面的变量则需要传入key；如果数组和target是同一个类则需要实现该类的__lt__, __gt__和__eq__）
    :param mode: 0为二分查找，1为左边界搜索，2为右边界搜索
    :param key: 搜索时用什么值进行比较
    :link: https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array/solution/er-fen-cha-zhao-suan-fa-xi-jie-xiang-jie-by-labula/
    :return:
    """
    if key is None:  # 如果没指定，那么生成默认的key函数
        key = lambda element: element
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if key(nums[mid]) < target:
            left = mid + 1
        elif key(nums[mid]) > target:
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


class BinaryIndexTree:
    # 树状数组。适用于sum()调用频繁的情况
    def __init__(self, array: list):
        self._array = [0] + array
        for i in range(1, len(self._array)):
            j = i + self._lowbit(i)
            if j < len(self._array):
                self._array[j] += self._array[i]

    def __getitem__(self, item: int):
        return self.sum(item, item + 1)

    def __setitem__(self, idx: int, val: int):
        prev = self.sum(idx, idx + 1)  # 原来的值
        idx += 1
        val -= prev  # 要增加的值
        while idx < len(self._array):
            self._array[idx] += val
            idx += self._lowbit(idx)

    def __len__(self):
        return len(self._array) - 1

    def _lowbit(self, x: int) -> int:
        return x & (-x)

    def sum(self, start: int, stop: int) -> int:
        return self.sumBefore(stop) - self.sumBefore(start)

    def sumBefore(self, stop=0) -> int:
        if stop < 1:
            stop = len(self._array) - 1
        res = 0
        while stop > 0:
            res += self._array[stop]
            stop -= self._lowbit(stop)
        return res


def mergeSort(nums: list):
    def merge(start, mid, end):
        i, j, mergedList = start, mid + 1, []
        while i <= mid and j <= end:
            if nums[i] <= nums[j]:  # 左边的小
                mergedList.append(nums[i])
                i += 1
            else:  # 右边的小
                # self.cnt += mid - i + 1
                mergedList.append(nums[j])
                j += 1
        while i <= mid:
            mergedList.append(nums[i])
            i += 1
        while j <= end:
            mergedList.append(nums[j])
            j += 1

        for i in range(len(mergedList)):
            nums[start + i] = mergedList[i]

    def _mergeSort(start, end):
        if start >= end:
            return
        mid = (start + end) // 2
        _mergeSort(start, mid)  # 分为[start, mid], [mid + 1, end]
        _mergeSort(mid + 1, end)
        merge(start, mid, end)

    _mergeSort(0, len(nums) - 1)


# endregion

if __name__ == '__main__':
    ans=TreeUtil.createTreeByPreInOrder('ABCDEFGHI','BDCAFEHIG')
    print(TreeUtil.postOrderTraversal(ans))

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
