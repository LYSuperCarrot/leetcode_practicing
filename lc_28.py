class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        len_needle = len(needle)
        if len_needle == 0:
            return 0
        
        for i in range(len(haystack)-len_needle+1):
            if haystack[i:i+len_needle] == needle:
                return i
        return -1



haystack = "hell"
needle = "ll"
sol = Solution()
print(sol.strStr(haystack, needle)) 