
class ListNode:
    def __init__(self, item = None, next = None):
        self.item = item
        self.next = next

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
a.next = b
b.next = c
print(a.next.item)

class Stack:
    def __init__(self):
        self.top = None
    
    def is_empty(self):
        return self.top is None
    
    def push(self, item):
        self.top = ListNode(item, self.top)
    
    def top(self):
        if self.top is None:
            print("empty")
            return
        return self.top.item
    
    def pop(self):
        if self.top is None:
            print("empty")
            return
        t = self.top
        self.top = self.top.next
        return t.item

# 头插法
def creat_linklist_head(li):
    head = ListNode(li[0])
    for element in li[1:]:
        node = ListNode(element)
        node.next = head
        head = node
    return head

def create_linklist_tail(li):
    tail = ListNode(li[0])
    for element in li[1:]:
        node = ListNode(element)
        tail.next = node
        tail = node
    return tail


