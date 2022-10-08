# 题目：2296.设计一个文本编辑器
# 难度：HARD
# 最后提交：2022-06-05 13:10:02 +0800 CST
# 语言：python3
# 作者：ZrjaK

class TextEditor:

    def __init__(self):
        self.s = []
        self.t = []


    def addText(self, text: str) -> None:
        for i in text:
          self.s.append(i)

    def deleteText(self, k: int) -> int:
        s = self.s
        if len(s) < k:
            k = len(s)
        for i in range(k):
            s.pop()
        return k

    def cursorLeft(self, k: int) -> str:
        s = self.s
        t = self.t
        if len(s) < k:
            k = len(s)
        for i in range(k):
            t.append(s.pop())
        return "".join(s[-min(10, len(s)):])

    def cursorRight(self, k: int) -> str:
        s = self.s
        t = self.t
        if len(t) < k:
            k = len(t)
        for i in range(k):
            s.append(t.pop())
        return "".join(s[-min(10, len(s)):])


# Your TextEditor object will be instantiated and called as such:
# obj = TextEditor()
# obj.addText(text)
# param_2 = obj.deleteText(k)
# param_3 = obj.cursorLeft(k)
# param_4 = obj.cursorRight(k)