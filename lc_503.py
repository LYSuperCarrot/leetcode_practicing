class Solution:
    def nextGreaterElements(self, nums):
        num_length = len(nums)
        res_list = [-1 for _ in range(num_length)]
        stack = []

        double_nums = nums + nums
        for i, num in enumerate(double_nums):
            while stack and nums[stack[-1]] < num:
                res_list[stack[-1]] = num
                stack.pop()
            if i < num_length:
                stack.append(i)
        return res_list

sol = Solution()
nums = [1,2,1]
print(sol.nextGreaterElements(nums))