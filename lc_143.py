class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        cur = head
        nodeList = []
        while cur:
            nodeList.append(cur)
            cur = cur.next
        left = 0
        right = len(nodeList) - 1
        while left < right:
            nodeList[left].next = nodeList[right]
            left += 1
            nodeList[right].next = nodeList[left]
            right -= 1
        nodeList[left].next = None

p1 = ListNode(1)
p2 = ListNode(2)
p3 = ListNode(3)
p4 = ListNode(4)
p1.next = p2
p2.next = p3
p3.next = p4
head = p1

sol = Solution()
sol.reorderList(head)