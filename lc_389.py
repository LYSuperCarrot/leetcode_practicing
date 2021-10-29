class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        return chr(sum(map(ord, t)) - sum(map(ord, s)))

s = "abcd"
t = "abcde"
sol = Solution()
ch = sol.findTheDifference(s, t)
print(ch)