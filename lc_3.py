class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # solution 1
        # li = []
        # max_num = 0
        # for s_str in s:
        #     for i, li_str in enumerate(li):
        #         if li_str == s_str:
        #             li = li[i+1:]
        #     li.append(s_str)
        #     if max_num < len(li):
        #         max_num += 1
        # return max_num
        
        # solution 2
        dirs = {}
        i, ans = -1, 0
        for j in range(len(s)):
            if s[j] in dirs:
                i = max(i, dirs[s[j]])
            ans = max(ans, j - i)
            dirs[s[j]] = j
        return ans

s = " "
sol = Solution()
print(sol.lengthOfLongestSubstring(s))