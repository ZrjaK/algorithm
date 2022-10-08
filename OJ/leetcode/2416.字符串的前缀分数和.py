# 题目：2416.字符串的前缀分数和
# 难度：HARD
# 最后提交：2022-09-18 11:12:19 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        tree = Trie()
        for s in words:
            tree.insert(s)
        res = []
        for s in words:
            res.append(tree.search(s))
        return res
        
        
        
class Trie:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False
        self.v = 0
    def search(self, prefix: str):
        res = 0
        node = self
        for ch in prefix:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                return 0
            res += node.v
            # print(ch, node.v)
            node = node.children[ch]
        res += node.v
        return res

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord("a")
            if not node.children[ch]:
                node.children[ch] = Trie()
            
            node = node.children[ch]
            node.v += 1
        node.isEnd = True