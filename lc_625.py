
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findDuplicateSubtrees(self, root):
        result = []
        mp = {}
        self.helper(root, result, mp)
        return result
    
    def helper(self, root, result, mp):
        if not root:
            return "#"
        string = str(root.val) + ' ' + self.helper(root.left, result, mp) + ' ' + self.helper(root.right, result, mp)
        count = 0
        if string in mp:
            count = mp[string]
        else:
            mp[string] = 0
        if count == 1:
            result.append(root)
        mp[string] += 1
        return string

a = TreeNode(1)
b = TreeNode(2)
c = TreeNode(3)
d = TreeNode(4)
e = TreeNode(2)
f = TreeNode(4)
g = TreeNode(4)
a.left = b
a.right = c
b.left = d
c.left = e
c.right = f
e.left = g

sol = Solution()
print(sol.findDuplicateSubtrees(a))