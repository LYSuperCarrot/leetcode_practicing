class Solution:
    def findPairs(self, nums, k):
        count = 0
        hash_table = {}
        for num in nums:
            if num in hash_table:
                hash_table[num] += 1
            
            if num+k not in hash_table:
                hash_table[num+k] = 0
            if num-k not in hash_table:
                hash_table[num-k] = 0
        for key in hash_table:
            if hash_table[key] >= 1:
                count += 1
        return count

nums = [1,2,4,4,3,3,0,9,2,3]
k = 3
sol = Solution()
print(sol.findPairs(nums, k))