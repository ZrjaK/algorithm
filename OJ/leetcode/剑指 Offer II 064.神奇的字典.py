# 题目：剑指 Offer II 064.神奇的字典
# 难度：MEDIUM
# 最后提交：2022-10-08 12:10:52 +0800 CST
# 语言：python3
# 作者：ZrjaK

class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = set()


    def buildDict(self, dictionary: List[str]) -> None:
        self.d = set(dictionary)

    def search(self, searchWord: str) -> bool:
        n = len(searchWord)
        for i in range(n):
            for j in range(26):
                if searchWord[i] != chr(j+97) and searchWord[:i] + chr(j+97) + searchWord[i+1:] in self.d:
                    return True
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)