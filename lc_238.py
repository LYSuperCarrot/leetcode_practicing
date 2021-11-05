class Solution:
    def productExceptSelf(self, nums):
        left, right = 1, 1
        length = len(nums)
        res = [1 for _ in range(length)]
        for i in range(length):
            res[i] *= left
            left *= nums[i]

            res[length-i-1] *= right
            right *= nums[length-i-1]
        
        return res

sol = Solution()
nums = [1,2,3,4]
res = sol.productExceptSelf(nums)
print(res)