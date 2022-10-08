# 题目：1813.句子相似性 III
# 难度：MEDIUM
# 最后提交：2022-06-13 15:35:35 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        split1 = sentence1.split(' ')
        split2 = sentence2.split(' ')
        while split1 and split2:
            if split1[0] == split2[0]:
                split1.pop(0)
                split2.pop(0)
            elif split1[-1] == split2[-1]:
                split1.pop()
                split2.pop()
            else:
                return False
        return not split1 or not split2