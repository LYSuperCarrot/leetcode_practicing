import copy
nums = [1, 2, 3]

class Solution:
    def subsets(self, nums):
        # 扩展法
        # results = [[]]
        # for num in nums:
        #     temp = []
        #     for res in results:
        #         
        #         temp.append(res+[num])
        #     for t in temp:
        #         results.append(t)
        # return result

        # 回溯法: 剪枝，一旦发现子集长度==当前长度，减掉多余的枝
        # result = []
        # result.append([])
        # for i in range(1, len(nums)):
        #     self.backtracking(nums, result, i, 0, [])


        # DFS
        result = []
        self.dfs(nums, result, 0, [])
        return result
    

    def dfs(self, nums, result, index, subset):
        result.append(copy.deepcopy(subset))
        if index == len(nums):
            for i in range(index, len(nums)):
                subset.append(nums[i])
                self.dfs(nums, result, i+1, subset)
                subset.pop()
    
    
    
    def backtracking(self, nums, result, length, index, subset):
        if len(subset) == length:
            temp = copy.deepcopy(subset)
            result.append(temp)
            return
        
        for i in range(index, len(nums)):
            subset.append(nums[i])
            self.backtracking(nums, result, length, i+1, subset)
            subset.pop()

        

