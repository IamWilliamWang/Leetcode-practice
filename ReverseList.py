from test_script import ListNode, ListUtil


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        newHead = ListNode(0)
        for node in ListUtil.iterator(head):
            node.next = newHead.next
            newHead.next = node
        return newHead.next
