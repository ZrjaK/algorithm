# 题目：843.猜猜这个单词
# 难度：HARD
# 最后提交：2022-09-17 13:08:43 +0800 CST
# 语言：python3
# 作者：ZrjaK

# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master:
#     def guess(self, word: str) -> int:

class Solution:
    def findSecretWord(self, wordlist: List[str], master: 'Master') -> None:
        def check(word1, word2):
            return sum([word1[i] == word2[i] for i in range(6)])
        
        for _ in range(30):
            i = random.randint(0, len(wordlist)-1)
            length = master.guess(wordlist[i])
            if length == 6:
                return
            wordlist = [word for word in wordlist if check(word, wordlist[i])==length]