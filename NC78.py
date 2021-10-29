# 输入一个长度为n链表，反转链表后，输出新链表的表头。

# 数据范围 
# 要求：空间复杂度 O(1)O(1) ，时间复杂度 O(n)O(n) 。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        cur_node = None
        next_node = None
        while pHead:
            next_node = pHead.next
            pHead.next = cur_node
            cur_node = pHead
            pHead = next_node
 
        return cur_node

