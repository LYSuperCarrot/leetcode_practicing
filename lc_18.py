class Solution:
    def fourSum(self, nums, target):
        n = len(nums)
        if n < 4:
            return []
        nums.sort()
        res = []
        left = 0
        right = n - 1
        while left < right:
            inner_left = left + 1
            inner_right = right - 1
            if left > 1 and nums[left] == nums[left - 1]:
                left += 1
                continue
            while inner_left < inner_right:
                total = nums[left] + nums[right] + nums[inner_left] + nums[inner_right]
                diff = total - target
                if diff < 0:
                    inner_left += 1
                elif diff > 0:
                    inner_right -= 1
                else:
                    res.append([nums[left], nums[inner_left], nums[inner_right], nums[right]])
                    while inner_left != inner_right and nums[inner_left] == nums[inner_left + 1]: inner_left += 1
                    while inner_left != inner_right and nums[inner_right] == nums[inner_right - 1]: inner_right -= 1
                    inner_left += 1
                    inner_right -= 1
            cov_total = nums[left] + nums[right]
            cov_diff = cov_total - target
            if cov_diff > 0:
                right -= 1
            elif cov_diff < 0:
                left += 1
            else:
                left += 1
                right -= 1
        return res

sol = Solution()
nums = [2,2,2,2,2]
target = 8
print(sol.fourSum(nums, target))