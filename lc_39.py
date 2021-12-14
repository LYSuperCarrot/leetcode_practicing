class Solution:
    def combinationSum(self, candidates, target):
        candidates.sort()
        res = []
        path = []
        def backtracking(candidates, target, StartIndex):
            if sum(path) == target:
                res.append(path[:])
                return
            elif sum(path) > target:
                return
            for i in range(StartIndex, len(candidates)):
                path.append(candidates[i])
                backtracking(candidates, target, i)
                # path.pop()
        backtracking(candidates, target, 0)
        return res

sol = Solution()
candidates = [2,3,6,7]
target = 7
sol.combinationSum(candidates, target)