# 题目：929.独特的电子邮件地址
# 难度：EASY
# 最后提交：2021-11-02 19:24:57 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        res = []
        for i in emails:
            if "+" in i:
                s = i.split('+')[0].replace(".", "") + i[i.find("@"):]
            else:
                s = i.split("@")[0].replace(".", "") + i[i.find("@"):]
            res.append(s)
        return len(set(res))