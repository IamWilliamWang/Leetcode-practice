# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def _listLen(self, headNode: ListNode) -> int:
        """
        计算链表长度
        """
        len = 0
        while headNode is not None:
            len += 1
            headNode = headNode.next
        return len

    def addTwoNumbers(self, list1: ListNode, list2: ListNode) -> ListNode:
        len1, len2 = self._listLen(list1), self._listLen(list2)
        if len1 < len2:  # 使得list1为最长的数字，以便后面处理
            list1, list2 = list2, list1
            len1, len2 = len2, len1
        stack = []  # 收集各个节点的栈
        p1, p2 = list1, list2  # 指向两个链表的pointer
        for i in range(len1 - len2):  # 跳过不用加的这部分
            stack.append(p1)
            p1 = p1.next
        while p1 is not None:  # 先把每个数字加起来
            p1.val += p2.val
            stack.append(p1)
            p1 = p1.next
            p2 = p2.next
        while len(stack) > 1:  # 一直出栈并查看是否需要向前进位
            nowNode = stack.pop()
            if nowNode.val >= 10:
                nowNode.val -= 10
                stack[-1].val += 1
        if list1.val >= 10:  # 首位如果是10就在它前面插一个新的1
            list1.val -= 10
            newNode = ListNode(1)
            newNode.next = list1
            list1 = newNode
        return list1


def generator(l: list):
    headNode = ListNode(l[0])
    p = headNode
    for i in range(1, len(l)):
        newNode = ListNode(l[i])
        p.next = newNode
        p = newNode
    return headNode


l1 = generator([1])
l2 = generator([9, 9, 9])
print(Solution().addTwoNumbers(l1, l2))
print(l1, l2)
