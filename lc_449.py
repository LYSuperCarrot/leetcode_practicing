from DataStructure_tree import in_order


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Codec:

    def serialize(self, root) -> str:
        """Encodes a tree to a single string.
        """
        if not root:
            return ""
        stack = [root]
        res = []
        
        while stack:
            curNode = stack.pop()
            res.append(str(curNode.val))
            if curNode.right:
                stack.append(curNode.right)
            
            if curNode.left:
                stack.append(curNode.left)
            
        return ','.join(res)
        

        

    def deserialize(self, data: str):
        """Decodes your encoded data to tree.
        """
        if not data:
            return None
        pre_o = list(map(int, data.split(',')))
        in_o = sorted(pre_o)

        def buildTree(pre_o, in_o):
            mid = pre_o[0]
            root = TreeNode(mid)
            i = in_o.index(mid)
            root.left = buildTree(pre_o[1:i+1], in_o[:i])
            root.right = buildTree(pre_o[i+1:], in_o[i+1:])
            return root
        return buildTree(pre_o, in_o)

sol = Codec()
a = TreeNode(2)
b = TreeNode(1)
c = TreeNode(3)
a.left = b
a.right = c
print(sol.serialize(a))
