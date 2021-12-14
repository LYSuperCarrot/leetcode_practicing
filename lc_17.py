class Solution:
    def __init__(self):
        self.answers = []
        self.letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

    def letterCombinations(self, digits: str):
        self.answers.clear()
        if not digits: return []
        self.backtracking(digits, 0, '')
        return self.answers
    
    def backtracking(self, digits: str, index: int, answer: str) -> None:
        # 回溯函数没有返回值
        # Base Case
        if index == len(digits):    # 当遍历穷尽后的下一层时
            self.answers.append(answer)
            return 
        # 单层递归逻辑  
        letters: str = self.letter_map[digits[index]]
        for letter in letters:
            self.backtracking(digits, index + 1, answer + letter)    # 递归至下一层 + 回溯

sol = Solution()
print(sol.letterCombinations("23"))