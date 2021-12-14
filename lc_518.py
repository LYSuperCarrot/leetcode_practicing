class Solution:
    def change(self, amount: int, coins) -> int:
        dp = [0 for _ in range(amount+1)]
        dp[0] = 1
        # 组合
        # for i in range(len(coins)):
        #     for j in range(coins[i], amount+1):
        #         dp[j] += dp[j-coins[i]]
        
        # 排列
        for j in range(amount+1):
            for i in range(len(coins)):
                dp[j] += dp[j-coins[i]]
        return dp[-1]

sol = Solution()
amount = 5
coins = [1,2,5]
print(sol.change(amount, coins))