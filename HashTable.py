
# 链表
class LinkList:
    class Node:
        def __init__(self, item=None, next=None):
            self.item = item
            self.next = next
    
    class LinkListIterator:
        def __init__(self, node):
            self.node = node
        
        def __next__(self):
            if self.node:
                cur_node = self.node
                self.node = cur_node.next
                return cur_node.item
            else:
                raise StopIteration
        
        def __iter__(self):
            return self

    def __init__(self, iterable=None):
        self.head = None
        self.tail = None
        if iterable:
            self.extend(iterable)
    
    def extend(self, iterable):
        for obj in iterable:
            self.append(obj)

    def append(self, obj):
        s = LinkList.Node(obj)
        if not self.head:
            self.head = s
            self.tail = s
        else:
            self.tail.next = s
            self.tail = s
    
    def find(self, obj):
        for n in self:
            if n == obj:
                return True
        else:
            return False

    
    def __iter__(self):
        return self.LinkListIterator(self.head)
    
    def __repr__(self) -> str:
        return "<<"+",".join(map(str, self))+">>"

# 哈希表
class HashTable:
    def __init__(self, maxsize=101):
        self.size = maxsize
        self.T = [LinkList() for _ in range(self.size)]
    
    def h(self, k):
        return k % self.size
    
    def find(self, k):
        i = self.h(k)
        return self.T[i].find(k)
    
    def insert(self, k):
        i = self.h(k)
        if self.find(k):
            print("Duplicated Insert")
        else:
            self.T[i].append(k)
   

ht = HashTable(10)
ht.insert(0)
ht.insert(1)
ht.insert(11)
print(",".join(map(str, ht.T)))




