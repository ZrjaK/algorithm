# 题目：2424.最长上传前缀
# 难度：MEDIUM
# 最后提交：2022-10-01 22:38:47 +0800 CST
# 语言：python3
# 作者：ZrjaK

class LUPrefix:

    def __init__(self, n: int):
        self.arr = [0] * (n+1)
        self.cnt = 0

    def upload(self, video: int) -> None:
        self.arr[video] = 1
        while self.cnt+1 < len(self.arr) and self.arr[self.cnt+1]:
            self.cnt += 1
        

    def longest(self) -> int:
        return self.cnt


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()