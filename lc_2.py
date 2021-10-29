# 两数字相加

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # method 1
        head = ListNode(0)
        tail = head
        carry = 0
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            tail.next = ListNode(s%10)
            tail = tail.next
            if(l1 != None):l1=l1.next
            if(l2 != None):l2=l2.next
        
        if carry > 0:
            tail.next = ListNode(1)
        return head.next



        
        # method 2
        # num1_li = []
        # num2_li = []
        # while l1:
        #     num1_li.append(l1.val)
        #     l1 = l1.next
        
        # while l2:
        #     num2_li.append(l2.val)
        #     l2 = l2.next
        
        # num1 = 0
        # num2 = 0
        # for i in range(len(num1_li)):
        #     num1 += 10**i + num1_li[i]
        
        # for j in range(len(num2_li)):
        #     num2 += 10**j + num1_li[j]
        
        # result = num1 + num2
        # result_li = self.val2li(result)
        # result_node = self.li2node(result_li)
        # return result_node
        #


    
    def val2li(self, val):
        li = []
        while val != 0:
            mod = val % 10
            li.append(mod)
            val = (val - mod) / 10
        return li
        

    def li2node(self, li):
        head = ListNode(li[0])
        tail = head
        if len(li) > 1:
            for i in range(1, len(li)):
                node = ListNode(li[i])
                tail.next = node
                tail = node
        return head
    
    def display_node(self, head):
        while head:
            print(head.val)
            head = head.next
        




sol = Solution()
l1 = [2, 4, 3]
l2 = [5, 6, 4]
l1_head = sol.li2node(l1)
l2_head = sol.li2node(l2)
head = sol.addTwoNumbers(l1_head, l2_head)
sol.display_node(head)


