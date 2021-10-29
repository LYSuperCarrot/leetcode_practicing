class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        num = 0
        s_str = ""
        match = {'a', 'e', 'i', 'o', 'u'}
        max_num = 0
        for i in range(k):
            s_str += s[i]
            if s[i] in match:
                num += 1
                if max_num < num:
                    max_num = num
        for i in range(k, len(s)):
            s_str += s[i]
            if s[i] in match:
                num += 1
            if s_str[0] in match:
                num -= 1
            s_str = s_str[1:]
            if max_num < num:
                max_num = num
        
        return max_num

sol = Solution()
s = "leetcode"
k = 3
i = sol.maxVowels(s, k)
print(i)