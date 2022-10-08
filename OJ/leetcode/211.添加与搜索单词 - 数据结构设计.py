# 题目：211.添加与搜索单词 - 数据结构设计
# 难度：MEDIUM
# 最后提交：2022-08-18 16:25:18 +0800 CST
# 语言：python3
# 作者：ZrjaK

class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEnd = False

    def insert(self, word: str) -> None:
        node = self
        for ch in word:
            ch = ord(ch) - ord('a')
            if not node.children[ch]:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True
class WordDictionary:
    def __init__(self):
        self.trieRoot = TrieNode()

    def addWord(self, word: str) -> None:
        self.trieRoot.insert(word)

    def search(self, word: str) -> bool:
        def dfs(index: int, node: TrieNode) -> bool:
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch != '.':
                child = node.children[ord(ch) - ord('a')]
                if child and dfs(index + 1, child):
                    return True
            else:
                for child in node.children:
                    if child and dfs(index + 1, child):
                        return True
            return False

        return dfs(0, self.trieRoot)