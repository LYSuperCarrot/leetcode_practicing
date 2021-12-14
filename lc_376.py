class Solution:
    def wiggleMaxLength(self, nums) -> int:
        length = len(nums)
        if length == 0:
            return 0

        nums1 = [nums[0]]
        for i in range(1, length):
            if nums[i] != nums[i-1]:
                nums1.append(nums[i])
        n = len(nums1)
        if n <= 2:
            return n
        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            if (nums1[i-1]-nums1[i-2]) * (nums1[i]-nums1[i-1]) < 0:
                dp[i] = dp[i-1] + 1
            else:
                dp[i] = dp[i-1]
        return dp[n-1]

nums = [1,7,4,9,2,5]
sol = Solution()
print(sol.wiggleMaxLength(nums))