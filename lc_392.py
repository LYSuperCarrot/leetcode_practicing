class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        s_check = ""
        for ch in s:
            while i < len(t):
                if t[i] == ch:
                    s_check += t[i]
                    i += 1
                    break
                else:
                    i += 1
        if len(s_check) == len(s):
            return True
        else:
            return False

sol = Solution()
s = "aaaaaa"
t = "bbaaaa"
print(sol.isSubsequence(s, t))