from collections import deque
# 模拟系统文件
class Node:
    def __init__(self, name=None, type='dir'):
        self.name = name
        self.type = type
        self.children = []
        self.parent = None
    
    def __str__(self):
        return self.name

class FileSystemTree:
    def __init__(self):
        self.root = Node("/")
        self.now = self.root
    
    def mkdir(self, dir_name):
        if dir_name[-1] != '/':
            dir_name += '/'
        node = Node(dir_name)
        self.now.children.append(node)
        node.parent = self.now
    
    def ls(self):
        return self.now.children
    
    def cd(self, dir_name):
        if dir_name[-1] != '/':
            dir_name += '/'
        if dir_name == '../':
            self.now = self.now.parent
            return
        
        for child in self.now.children:
            if child.name == dir_name:
                self.now = child
                return
            else:
                raise ValueError("Invalid Dir Name")
    
# 二叉树
class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None
        self.parent = None
        

## 二叉树遍历
# a = BiTreeNode("A")
# b = BiTreeNode("B")
# c = BiTreeNode("C")
# d = BiTreeNode("D")
# e = BiTreeNode("E")
# f = BiTreeNode("F")
# g = BiTreeNode("G")

# e.lchild = a
# e.rchild = g
# a.rchild = c
# c.lchild = b
# c.rchild = d
# g.rchild = f 

# root = e

def pre_order(root):
    if root:
        print(root.data, end=",")
        pre_order(root.lchild)
        pre_order(root.rchild)

def pre_order_no_rec(root):
    if not root:
        return []
    
    stack = [root]
    res = []
    while stack:
        res.append(stack[-1].val)
        node = stack.pop()
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
        
    return res

def in_order(root):
    if root:
        in_order(root.lchild)
        print(root.data, end=",")
        in_order(root.rchild)

def in_order_no_rec(root):
    stack, res = [], []
    cur = root
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
    return res

def post_order(root):
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=",")

def post_order_no_rec(root):
    res, stack = [], []
    cur = root
    done = None
    while stack or cur:
        if cur:
            stack.append(cur)
            cur = cur.left
        else:
            cur = stack[-1]
            if cur.right and cur.right != done:
                cur = cur.right
                continue
            cur = stack.pop()
            res.append(cur.val)
            done = cur
            cur = None
    return res

def level_order(root):
    queue = deque()
    queue.append(root)
    while len(queue) > 0:
        node = queue.popleft()
        print(node.data, end=',')
        if node.lchild:
            queue.append(node.lchild)
        if node.rchild:
            queue.append(node.rchild)


# level_order(root)

# 二叉搜索树：满足根节点大于左侧子节点小于右侧子节点的二叉树
class BST:
    def __init__(self, li=None):
        self.root = None
        if li:
            for val in li:
                self.insert_no_rec(val)
    
    def insert_no_rec(self, val):
        p = self.root
        if not p:
            self.root = BiTreeNode(val)
            return
        
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = BiTreeNode(val)
                    p.lchild.parent = p
            
            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = BiTreeNode(val)
                    p.rchild.parent = p
            else:
                return

    def insert(self, node, val):
        if not node:
            node = BiTreeNode(val)
        elif val < node.data:
            self.insert(node.lchild, val)
            node.lchild.parent = node
        elif val > node.data:
            self.insert(node.rchild, val)
            node.rchild.parent = node
    
    def query_no_rec(self, val):
        p = self.root
        while p:
            if val < p.data:
                p = p.lchild
            elif val > p.data:
                p = p.rchild
            else:
                return p
        else:
            return None
    
    def query(self, node, val):
        if not node:
            return None
        
        if val < node.data:
            self.query(node.lchild, val)
        elif val > node.data:
            self.query(node.rchild, val)
        else:
            return node
    
    def pre_order(self, root):
        if root:
            print(root.data, end=",")
            pre_order(root.lchild)
            pre_order(root.rchild)

    def in_order(self, root):
        if root:
            in_order(root.lchild)
            print(root.data, end=",")
            in_order(root.rchild)

    def post_order(self, root):
        if root:
            post_order(root.lchild)
            post_order(root.rchild)
            print(root.data, end=",")

    def __remove_node_1(self, node):
        # 如果这个node是叶子节点
        p = node.parent
        if not p:
            self.root = None
        else:
            if p.lchild == node:
                p.lchild = None
            elif p.rchild == node:
                p.rchild = None

    def __remove_node_21(self, node):
        # node是父亲节点，并且没有右孩子
        p = node.parent
        if not p:
            self.root = node.lchild
            node.lchild.parent = None
        else:
            if p.lchild == node:
                p.lchild = node.lchild
                node.lchild.parent = p
            elif p.rchild == node:
                p.rchild = node.lchild
                node.lchild.parent = p

    
    def __remove_node_22(self, node):
        # node是父亲节点，并且没有左孩子
        p = node.parent
        if not p:
            self.root = node.rchild
            node.rchild.parent = None
        else:
            if p.lchild == node:
                p.lchild = node.rchild
                node.rchild.parent = p
            elif p.rchild == node:
                p.rchild = node.rchild
                node.rchild.parent = p

    def delete(self, val):
        if self.root:
            node = self.query_no_rec(val)
        
        if not node:
            return False
        else:
            # 如果这个node是叶子节点
            if not node.lchild and not node.rchild:
                self.__remove_node_1(node)
            # 如果这个node是父亲节点，并且没有右孩子
            elif not node.rchild:
                self.__remove_node_21(node)
            # 如果这个node是父亲节点，并且没有左孩子
            elif not node.lchild:
                self.__remove_node_22(node)
            # node是父亲节点，且两个孩子都有
            else:
                min_node = node.rchild
                while min_node.lchild:
                    min_node = min_node.lchild
                node.data = min_node.data
                if min_node.rchild:
                    self.__remove_node_22(min_node)
                else:
                    self.__remove_node_1(min_node)



bst = BST([4,6,7,9,2,1,3,5,8])
bst.in_order(bst.root)
print("")

bst.delete(4)
bst.delete(8)
bst.in_order(bst.root)

# 二叉平衡树，AVL树:自平衡的二叉搜索树，根的左右子树高度差不超过1
# 并且根的左右子树都是二叉平衡树
class AVLNode(BiTreeNode):
    def __init__(self, data):
        BiTreeNode.__init__(self, data)
        self.bf = 0 # bf > 0, 说明该node的右侧高度高。
        # bf < 0， 说明该node的左侧高度高


class AVLTree(BST):
    def __init__(self, li=None):
        super().__init__(li=li)
    
    def rotate_right(self, p, c):
        s2 = c.rchild
        p.lchild = s2
        if s2:
            s2.parent = p
        c.rchild = p
        p.parent = c

        p.bf = 0
        c.bf = 0
        return c
        

    def rotate_left(self, p, c):
        s2 = c.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        c.lchild = p
        p.parent = c

        c.bf = 0
        p.bf = 0
        return c
    


    def rotate_right_left(self, p, c):
        g = c.lchild
        s2 = g.lchild
        p.rchild = s2
        if s2:
            s2.parent = p
        g.lchild = p
        p.parent = g

        s3 = g.rchild
        c.lchild = s3
        if s3:
            s3.parent = c
        g.rchild = c
        c.parent = g
        

        if g.bf > 0:
            c.bf = 0
            p.bf = -1
        else:
            c.bf = 1
            p.bf = 0
        
        g.bf = 0
        return g


    def rotate_left_right(self, p, c):
        g = c.rchild

        s2 = g.lchild
        c.rchild = s2
        if s2:
            s2.parent = c
        g.lchild = c
        c.parent = g

        s3 = g.rchild
        p.lchild = s3
        if s3:
            s3.parent = p
        g.rchild = p
        p.parent = g

        if g.bf > 0:
            p.bf = 0
            c.bf = -1
        else:
            c.bf = 0
            p.bf = 1
        
        g.bf = 0
        return g

    def insert_no_rec(self, val):
        p = self.root
        node = None
        if not p:
            self.root = AVLNode(val)
            return
        
        while True:
            if val < p.data:
                if p.lchild:
                    p = p.lchild
                else:
                    p.lchild = AVLNode(val)
                    p.lchild.parent = p
                    node = p.lchild # node存储插入的节点
                    break

            elif val > p.data:
                if p.rchild:
                    p = p.rchild
                else:
                    p.rchild = AVLNode(val)
                    p.rchild.parent = p
                    node = p.rchild
                    break
            else:
                return
            
            while node.parent:
                if node.parent.lchild == node:
                    if node.parent.bf < 0:
                        g = node.parent.parent
                        x = node.parent
                        if node.bf > 0:
                            n = self.rotate_left_right(node.parent, node)
                        else:
                            n = self.rotate_right(node.parent, node)
                    elif node.parent.bf > 0:
                        node.parent.bf = 0
                        break
                    else:
                        node.parent.bf = -1
                        node = node.parent
                        continue
                else:
                    if node.parent.bf > 0:
                        g = node.parent.parent
                        x = node.parent
                        if node.bf < 0:
                            n = self.rotate_right_left(node.parent, node)
                        else:
                            n = self.rotate_left(node.parent, node)
                    elif node.parent.bf < 0:
                        node.parent.bf = 0
                        break
                    else:
                        node.parent.bf = -1
                        node = node.parent
                        continue
                
                n.parent = g
                if g:
                    if x == g.lchild:
                        g.lchild = n
                    else:
                        g.rchild = n
                    break
                else:
                    self.root = n
                    break









