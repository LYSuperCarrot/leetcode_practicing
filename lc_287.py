

class Solution:
    def moveZeroes(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solution 1
        # index = 0
        # for i in range(len(nums)):
        #     if nums[i] != 0:
        #         nums[index] = nums[i]
        #         index += 1
        # for j in range(index, len(nums)):
        #     nums[j] = 0

        # solution 2
        nums.sort(key=bool, reverse = True)

nums = [0,1,0,3,12]
sol = Solution()
sol.moveZeroes(nums)
print(nums)