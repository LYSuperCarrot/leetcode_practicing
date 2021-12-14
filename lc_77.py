class Solution:
    def __init__(self):
        self.res = []
        self.path = []
    def combine(self, n, k):
        self.backtracking(n, k, 1)
        return self.res

    def backtracking(self, n, k, startIndex):
        if len(self.path) == k:
            self.res.append(self.path[:])
            return
        for i in range(startIndex, n-(k-len(self.path)) + 2):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()

sol = Solution()
print(sol.combine(4,2))

