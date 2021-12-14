class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        left = 0
        right = left + k
        temp_window = nums[left: right+1]
        for i in range(len(temp_window)):
            for j in range(i+1, len(temp_window)):
                if abs(temp_window[i] - temp_window[j]) <= t:
                    return True
        right += 1
        left += 1
        while right <= len(nums)-1:
            temp_window = nums[left: right+1]
            new_item = temp_window[-1]
            for i in range(len(temp_window)-1):
                if abs(temp_window[i] - new_item) <= t:
                    return True
            right += 1
            left += 1
        return False

sol = Solution()
nums = [1,5,9,1,5,9]
k = 2 
t = 3
print(sol.containsNearbyAlmostDuplicate(nums, k, t))
