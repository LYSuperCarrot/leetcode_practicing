# class Solution:
#     def maxSubArray(self, nums) -> int:
#         res = nums[0]
#         sum = 0
#         for num in nums:
#             if sum > 0:
#                 sum += num
#             else:
#                 sum = num
#             res = max(res, sum)
#         return res

# class Solution:
#     def maxSubArray(self, nums):
#         return self.getMax(nums, 0, len(nums)-1)
    
#     def getMax(self, nums, left, right):
#         if left == right:
#             return nums[left]
#         mid = (left + right) // 2
#         leftmax = self.getMax(nums, left, mid)
#         rightmax = self.getMax(nums, mid+1, right)
#         crossmax = self.getCrossMax(nums, left, right)
#         return max(leftmax, rightmax, crossmax)
    
#     def getCrossMax(self, nums, left, right):
#         mid = (left + right) // 2
#         leftmax = nums[mid]
#         leftsum = leftmax
#         for i in range(mid-1, left-1, -1):
#             leftsum += nums[i]
#             leftmax = max(leftmax, leftsum)
        
#         rightmax = nums[mid+1]
#         rightsum = rightmax
#         for i in range(mid+2, right+1):
#             rightsum += nums[i]
#             rightmax = max(rightsum, rightmax)
#         return leftmax + rightmax

class Solution:
    def maxSubArray(self, nums) -> int:
        dp = [0]*len(nums)
        dp[0] = nums[0]
        result = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            result = max(result, dp[i])
        return result

nums = [5,4,-1,7,8]
sol = Solution()
max_sum = sol.maxSubArray(nums)
print(max_sum)
