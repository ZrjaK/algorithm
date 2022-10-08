# 题目：819.最常见的单词
# 难度：EASY
# 最后提交：2021-10-24 13:43:21 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = re.sub("\W", " ", paragraph).lower()
        paragraph = paragraph.split()
        for i in banned:
            while i in paragraph:
                paragraph.remove(i)
        
        return Counter(paragraph).most_common(1)[0][0]
