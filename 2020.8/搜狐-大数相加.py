from test_script import ListNode, ListUtil
from itertools import zip_longest


def iterator(headNode: ListNode):
    """
    链表的迭代器
    :param headNode 头节点
    :return: Iterator[ListNode]
    """
    while headNode is not None:
        nextNode = headNode.next  # 保证无论该节点发生什么都能按照原先的顺序进行遍历
        yield headNode
        headNode = nextNode


def add(root1: ListNode, root2: ListNode):
    overflow = 0
    resultRoot = ListNode(0)
    p = resultRoot
    for node1, node2 in zip_longest(iterator(root1), iterator(root2)):
        if not node1 or not node2:
            p.next = ListNode((node1 or node2).val)
            p = p.next
        else:
            p.next = ListNode(node1.val + node2.val + overflow)
            p = p.next
            if p.val >= 10:
                p.val -= 10
                overflow = 1
            else:
                overflow = 0
    return resultRoot.next


print(add(ListUtil.createListWithHead([2, 4, 3]).next, ListUtil.createListWithHead([5, 6, 4]).next))
