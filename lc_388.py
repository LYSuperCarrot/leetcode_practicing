import re
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        arr = input.split("\n")
        pattern = re.compile(r'[\t]*')
        stk = [0]

        res = 0
        for s in arr:
            # 计算当前位置有几个 "\t"
            level = len(pattern.match(s).group(0))
            cnt = len(s) - level
            if s.rfind('.') != -1:
                res = max(res, cnt + stk[level] + level)
            else:
                if level + 1 == len(stk):
                    # 压栈
                    stk.append(cnt + stk[level])
                else:
                    # 直接刷新，就不 pop 了
                    stk[level + 1] = cnt + stk[level]

        return res

input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"
sol = Solution()
print(sol.lengthLongestPath(input))