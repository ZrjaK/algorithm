# 题目：2241.设计一个 ATM 机器
# 难度：MEDIUM
# 最后提交：2022-04-17 05:43:28 +0800 CST
# 语言：python3
# 作者：ZrjaK

class ATM:

    def __init__(self):
        self.a = [0] * 5
        self.b = [20,50,100,200,500]
        self.d = [0] * 5

    def deposit(self, banknotesCount: List[int]) -> None:
        for i in range(5):
            self.a[i] += banknotesCount[i]

    def withdraw(self, amount: int) -> List[int]:
        q = []
        l = amount
        for i in range(4,-1,-1):
            x = min(l//self.b[i],self.a[i])
            l -= self.b[i] * x
            self.d[i] = x
        if l:
            q.append(-1)
            return q
        for i in range(5):
            q.append(self.d[i])
            self.a[i] -= self.d[i]
        return q


# Your ATM object will be instantiated and called as such:
# obj = ATM()
# obj.deposit(banknotesCount)
# param_2 = obj.withdraw(amount)