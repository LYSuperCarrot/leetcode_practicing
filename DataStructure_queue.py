# queue，队列, 从一端进，从另一端出
from collections import deque

q = deque([1,2,3], ) # 如果队满了，前面的自动出队
q.append(1) # 队尾进队（从右边进队）
q.popleft() # 队首出队

# 用于双向队列
q.appendleft(2) # 队首进队
q.pop() 		# 队尾出队

# 实现linux tail 命令，打印文件的最后n行
def tail(n):
	with open('test.txt', 'r') as f:
		q = deque(f, n)
		return q # 队列如果满了，前面的自动出队，所以tail中的n正好是队列中的n


class Queue:
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.front = 0
        self.rear = 0
    
    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError("Queue is filled")

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        return self.rear == self.front

    def is_filled(self):
        return (self.rear + 1) % self.size == self.front

