# 题目：804.唯一摩尔斯密码词
# 难度：EASY
# 最后提交：2021-10-24 13:04:46 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        d = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..'}
        return len(set("".join(itemgetter(*word)(d)) for word in words))