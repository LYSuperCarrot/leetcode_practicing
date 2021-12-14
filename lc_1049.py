class Solution:
    def lastStoneWeightII(self, stones):
        total_weight = sum(stones)
        target = total_weight // 2 
        dp = [[0 for _ in range(target+1)] for _ in range(len(stones))]
        for i in range(stones[0], len(dp)):
            dp[0][i] = stones[0]
        for i in range(len(dp)):
            dp[i][0] = 0
        
        for i in range(1, len(dp)):
            for j in range(i, len(dp[0])):
                if j >= stones[i]:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-stones[i]]+stones[i])
                else:
                    dp[i][j] = dp[i-1][j]
        return total_weight - 2*dp[-1][-1]

sol = Solution()
stones = [1,2]
sol.lastStoneWeightII(stones)