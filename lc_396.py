class Solution:
    def maxRotateFunction(self, nums) -> int:
        max_sum = -float('inf')
        for i in range(len(nums)):
            temp = nums[-1]
            nums[1:] = nums[:-1]
            nums[1] = temp
            cur_sum = self.F_function(nums)
            max_sum = max(max_sum, cur_sum)
        return max_sum 


    
    def F_function(self, A):
        sums = 0
        for i in range(len(A)):
            sums += i * A[i]
        return sums

sol = Solution()
A = [4,3,2,6]
max_num = sol.maxRotateFunction(A)
print(max_num)
