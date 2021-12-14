import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt_num = int(math.sqrt(c))
        for i in range(0, sqrt_num+1):
            for j in range(0, sqrt_num+1):
                if (i*i + j*j) == c:
                    return True
        return False

c = 4
sol = Solution()
print(sol.judgeSquareSum(c))