class Solution:
    def nextGreaterElement(self, nums1, nums2):
        stack = []
        hash_table = {}
        for n in nums2:
            while stack and stack[-1] < n:
                hash_table[stack.pop()] = n
            stack.append(n)
        return [hash_table.get(x, -1) for x in nums1]

sol = Solution()
nums1 = [4,1,2]
nums2 = [1,3,4,2]
li = sol.nextGreaterElement(nums1, nums2)
print(li)