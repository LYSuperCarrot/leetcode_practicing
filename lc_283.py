class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_loc = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_loc] = nums[zero_loc], nums[i]
                for k in range(len(nums)):
                    if nums[k] == 0:
                        zero_loc = k
                        break
        return nums

nums = [0,1,0,3,12]
nums1 = [0,0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums1)
print(nums1)