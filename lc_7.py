class Solution:
    def reverse(self, x: int) -> int:
        n = 0
        while x != 0:
            n = n*10 + x%10
            x = int(x/10)
        
        if n >= -2147483648 and n <= 2147483647:
            return n
        else:
            return 0

x = -123
sol = Solution()
print(sol.reverse(x))