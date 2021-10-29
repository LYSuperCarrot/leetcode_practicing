# 栈， 从一端进从一端出
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, element):
        return self.stack.append(element)
    
    def pop(self):
        return self.stack.pop()

    def gettop(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return None
    
    def is_empty(self):
        return len(self.stack) == 0

# stack = Stack()
# print(stack.is_empty())
# stack.push('hello')
# print(stack.stack)
# stack.push('world')
# print(stack.stack)
# stack.pop()
# print(stack.stack)

# 括号匹配问题
char_str = "(){}[{[()]}"

def brace_match(s):
    match = {'}':'{', ']':'[', ')':'('}
    stack = Stack()
    for ch in s:
        if ch in {'{', '[', '('}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.gettop() == match[ch]:
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False

print(brace_match(char_str))