class Solution:
    def diffWaysToCompute(self, expression):
        res = []
        for i in range(len(expression)):
            c = expression[i]
            if c == '+' or c == '-' or c == '*':
                res1 = self.diffWaysToCompute(expression[:i+1])
                res2 = self.diffWaysToCompute(expression[i+1:])
                for l in res1:
                    for r in res2:
                        if c == '+':
                            res.append(int(l)+int(r))
                        elif c == '-':
                            res.append(int(l)-int(r))
                        elif c == '*':
                            res.append(int(l)*int(r))
        if len(res) == 0:
            res.append(int(expression))
        return res

sol = Solution()

expression = "2-1-1"
print(sol.diffWaysToCompute(expression))
