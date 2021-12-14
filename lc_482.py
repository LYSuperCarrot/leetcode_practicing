class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        S = ""
        for ch in s:
            if ch != '-':
                S += ch
        length = len(S)
        first_len = length % k
        res = S[:first_len]
        i = first_len
        while i <= length-1:
            res += "-"
            res += S[i:i+k]
            i += k
        return res.upper()

S = "5F3Z-2e-9-w"
K = 4
sol = Solution()
print(sol.licenseKeyFormatting(S, K))