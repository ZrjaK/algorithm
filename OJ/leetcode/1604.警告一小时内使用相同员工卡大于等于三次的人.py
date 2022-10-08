# 题目：1604.警告一小时内使用相同员工卡大于等于三次的人
# 难度：MEDIUM
# 最后提交：2022-08-31 15:52:59 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        d = defaultdict(list)
        for name, time in zip(keyName, keyTime):
            t = time.split(":")
            d[name].append(60*int(t[0])+int(t[1]))
        res = []
        for name in d:
            d[name].sort()
            for i in range(2, len(d[name])):
                if d[name][i] - d[name][i-2] <= 60:
                    res.append(name)
                    break
        return sorted(res)