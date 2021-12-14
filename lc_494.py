# class Solution:
#     def findTargetSumWays(self, nums, target):
#         nums_sum = sum(nums)
#         if (nums_sum + target) % 2 == 1:
#             return 0
#         if target > nums_sum:
#             return 0
        
#         pos_sum = (sum(nums) + target) // 2
#         dp = [0] * (pos_sum+1)
#         dp[0] = 1
#         for i in range(len(nums)):
#             for j in range(pos_sum, nums[i]-1, -1):
#                 dp[j] += dp[j-nums[i]]
#         return dp[-1]


class Solution:
    def findTargetSumWays(self, nums, target):

        # dp[i][j]：使用 下标为[0, i]的nums[i]能够填满j（包括j）这么大容量的包，有dp[i][j]种方法。

        sumValue = sum(nums)
        if abs(target) > sumValue or (sumValue + target) % 2 == 1: return 0

        # 如果target为正，这里凑的时plus的bagsize，如果target为负，这里凑的是minus的bagsize
        bagSize = (sumValue + target) // 2

        #初始化二维dp数组
        dp = [[0 for _ in range(bagSize + 1)]for _ in range(len(nums))]

        # 背包容量为0时的唯一方法就是什么也不放
        for i in range(len(nums)):
            dp[i][0] = 1

        # 由于下面循环中i是从index = 1行开始的，我们要手动初始化index = 0的行
        if nums[0]==0: # 如果第一个值为0，那么+0还是-0都是0，所有有两种方法
            dp[0][0] = 2 
        else: # 不是0的话，就找到背包容量等于num[0]的位置，此时放一个num[0]就可以填满这个背包
            for j in range(bagSize+1):
                if j==nums[0]:
                    dp[0][j] = 1

        for i in range(1,len(nums)):
            for j in range(bagSize+1):
                if j<nums[i]:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j - nums[i]]

        return dp[len(nums)-1][bagSize]

sol = Solution()
nums = [0,0,0,0,1]
target = 1
print(sol.findTargetSumWays(nums, target))