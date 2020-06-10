from typing import List
from test_script import ListNode, ListUtil


class Solution:
    def reverseFirstKNode(self, head: ListNode, k: int, rollbackDependsOnK=False) -> ListNode:
        """
        反转链表的前k个节点，返回反转后的链表
        :param head: 头节点
        :param k: 前k个节点
        :param rollbackDependsOnK: k过大时是否回滚
        :return:
        """
        if k <= 1:  # k=0, 1时可以跳过所有步骤
            return head
        reversedCount = 0  # 已经反转的节点个数
        nullHead = ListNode(None)  # 新建一个空的头节点
        tailNode, headOfRestList = None, None  # 保存反转链表的尾部，顺序还正常链表的头部
        node = head
        while node is not None:
            if reversedCount == k:  # 终止条件
                break
            if nullHead.next is None:  # 反转链表是空的，则保存他的尾部
                tailNode = node
            headOfRestList = node.next  # 当前节点要脱离，保存下个节点作为顺序正常的头部
            # 头插法
            node.next = nullHead.next
            nullHead.next = node
            reversedCount += 1
            # 接着遍历后面的节点
            node = headOfRestList
        # 反转结束，只需要将反转链表.next=剩余的正常链表
        tailNode.next = headOfRestList
        if rollbackDependsOnK and reversedCount < k:
            return self.reverseFirstKNode(nullHead.next, reversedCount)
        return nullHead.next

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        """
        将链表每k个反转一次，返回最终的链表
        :param head: 头节点
        :param k: 前k个节点
        :return:
        """
        if k <= 1:
            return head
        head = self.reverseFirstKNode(head, k)  # 先颠倒头节点
        index = 1  # 表示第几个节点
        previous = head
        node = head.next
        while node is not None:
            # 只处理k的倍数的节点，其余的跳过
            while index % k != 0 and node is not None:
                index += 1
                previous = node
                node = node.next
            if node is None:
                break
            # 从当前开始，反转k个元素
            node = self.reverseFirstKNode(node, k, rollbackDependsOnK=True)
            previous.next = node  # 链接前面的尾和新的头，就不会丢失任何元素了
            node = node.next
            index += 1
        return head


print(str(Solution().reverseKGroup(ListUtil.createListWithHead([1, 2, 3, 4, 5]).next, 2)))
