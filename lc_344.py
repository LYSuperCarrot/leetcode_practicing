class Solution:
    def reverseWords(self, s: str) -> str:
        words = []
        word_s = 0
        word_e = 0
        n = len(s)
        while word_s < n:
            while word_s < n and s[word_s] == " ":
                word_s += 1
            word_e = word_s
            while word_e < n and s[word_e] != " ":
                word_e += 1
            words.append(s[word_s: word_e+1])

s = "  Bob  a  Loves  Alice   "

words = []
word_s = 0
word_e = 0
n = len(s)
while word_s < n:
    while word_s < n and s[word_s] == " ":
        word_s += 1
    word_e = word_s
    while word_e < n and s[word_e] != " ":
        word_e += 1
    if word_s != word_e:
        words.append(s[word_s: word_e])
    word_s = word_e

print(words)