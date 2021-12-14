class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_check = ""
        for char in s:
            if (char <= 'Z' and char >= 'A') or (char <= 'z' and char >= 'a'):
                char = self.return_lowercase(char)
                s_check += char
        return s_check

    
    def return_lowercase(self, char):
        if char <= 'Z' and char >= 'A':
            char = chr(ord(char) + 32)
        return char

sol = Solution()
s = "A man, a plan, a canal: Panama"
print(sol.isPalindrome(s))