class Solution:
    def __init__(self):
        self.count = 0
    def minMoves(self, nums):
        self.count = 0
        self.addOne(nums)
        return self.count
    
    def arr_equal(self, nums):
        temp = nums[0]
        for num in nums:
            if num != temp:
                return False
        return True
    
    def addOne(self, nums):
        if self.arr_equal(nums):
            return
        else:
            n = len(nums)
            max_num = -float('inf')
            max_loc = 0
            for i in range(n):
                if nums[i] > max_num:
                    max_loc = i
                    max_num = nums[i]
            
            for i in range(max_loc):
                nums[i] += 1
            for i in range(max_loc+1, n):
                nums[i] += 1
            
            self.count += 1
            self.addOne(nums)

nums = [1,2,3]
sol = Solution()
count = sol.minMoves(nums)
print(count)