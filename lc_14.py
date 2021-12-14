class Solution:
    def longestCommonPrefix(self, strs) -> str:
        # method 1
        # i = 0
        # common = ""
        # while True:
        #     for word in strs:
        #         if i >len(word):
        #             return word
        #         else:
        #             if len(common) == i:
        #                 common += word[i]
        #             else:
        #                 if common[i] != word[i]:
        #                     return common[:i]
        #     i += 1
        
        # method 2
        if not strs: return ""
        ss = list(map(set, zip(*strs)))
        res = ""
        for i, x in enumerate(ss):
            x = list(x)
            if len(x) > 1:
                break
            res += x[0]
        return res

        # method 3
        # if not strs: return ""
        # s1 = min(strs)
        # s2 = max(strs)
        # for i,x in enumerate(s1):
        #     if x != s2[i]:
        #         return s2[:i]
        # return s1

sol = Solution()
strs = ["flower","flow","flight"]
# print(sol.longestCommonPrefix(strs))
# print(list(map(set, zip(*strs))))
print(list(zip(*strs)))