class Solution:
    def find132pattern(self, nums) -> bool:
        stack = []
        last = -float('inf')
        
        if len(nums) < 3:
            return False
        
        for i in range(len(nums)-1, -1, -1):
            if nums[i] < last:
                return True
            if stack and nums[i] > stack[-1]:
                last = stack[-1]
            stack.append(nums[i])
            
        return False

sol = Solution()
nums = [1,2,3,4]
# nums = [3,1,4,2]
# nums = [-1,3,2,0]
# nums = [1,3,2,4,5,6,10]
print(sol.find132pattern(nums))