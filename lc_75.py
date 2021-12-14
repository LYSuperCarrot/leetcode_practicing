class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = len(nums)-1
        a = 0
        while left < right:
            while nums[a] != 1:
                if nums[a] == 0:
                    nums[a], nums[left] = nums[left], nums[a]
                    left += 1
                    a = left
                if nums[a] == 2:
                    nums[a], nums[right] = nums[right], nums[a]
                    right -= 1
            a += 1

sol = Solution()
nums = [2,0,2,1,1,0]
sol.sortColors(nums)