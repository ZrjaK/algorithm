# 题目：1032.字符流
# 难度：HARD
# 最后提交：2023-01-30 21:14:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            node = node.children[ch]
        node.isEnd = True

    def query(self, word):
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return False
            node = node.children[ch]
            if node.isEnd:
                return True
        return False


class StreamChecker:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for i in words:
            self.trie.insert(i[::-1])
        self.s = ""

    def query(self, letter: str) -> bool:
        self.s += letter
        return self.trie.query(self.s[::-1])

        


# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)