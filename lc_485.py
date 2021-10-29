class Solution:
    def findMaxConsecutiveOnes(self, nums):
        dirs = {}
        i, ans = -1, 0
        for j in range(len(nums)):
            dirs[nums[j]] = j
            if nums[j] != 1:
                i = max(i, dirs[nums[j]])
            ans = max(ans, j - i)
        return ans

li = [1,1,0,1,1,1]
sol = Solution()
print(sol.findMaxConsecutiveOnes(li))