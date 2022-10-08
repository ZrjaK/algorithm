# 题目：2227.加密解密字符串
# 难度：HARD
# 最后提交：2022-04-03 13:52:51 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Encrypter:

    def __init__(self, keys: List[str], values: List[str], dictionary: List[str]):
        self.d = {}
        self.df = {}
        for i, j in zip(keys,values):
            self.d[i] = j
            if not j in self.df.keys():
                self.df[j] = [i]
            else:
                self.df[j] += [i]

        self.t = [self.encrypt(i) for i in dictionary]

    def encrypt(self, word1: str) -> str:
        r = ""
        for i in word1:
            r += self.d[i]
        return r

    def decrypt(self, word2: str) -> int:
        return self.t.count(word2)


# Your Encrypter object will be instantiated and called as such:
# obj = Encrypter(keys, values, dictionary)
# param_1 = obj.encrypt(word1)
# param_2 = obj.decrypt(word2)