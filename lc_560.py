class Solution:
    def subarraySum(self, nums, k):
        sum, res, cul = 0, 0, {}
        cul[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in cul:
                res += cul[sum - k]
            if sum not in cul:
                cul[sum] = 0
            cul[sum] += 1
        return res

nums = [1,1,1]
k = 2
sol = Solution()
print(sol.subarraySum(nums, k))