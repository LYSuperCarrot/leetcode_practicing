class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(0, len(dp[0])):
            dp[1][i] = 1
        for i in range(0, len(dp)):
            dp[i][1] = 1

        for i in range(1, len(dp)):
            for j in range(1, len(dp[0])):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

sol = Solution()
print(sol.uniquePaths(3,7))