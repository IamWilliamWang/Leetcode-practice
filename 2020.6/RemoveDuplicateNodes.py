from test_script import ListNode, ListUtil


class Solution:
    def removeDuplicateNodes(self, head: ListNode) -> ListNode:
        result = []
        hashSet = set()
        for node in ListUtil.iterator(head):
            if node.val not in hashSet:
                result.append(node.val)
                hashSet.add(node.val)
        return ListUtil.createListWithHead(result).next
