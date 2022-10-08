# 题目：1600.王位继承顺序
# 难度：MEDIUM
# 最后提交：2022-08-20 15:54:32 +0800 CST
# 语言：python3
# 作者：ZrjaK

class ThroneInheritance:

    def __init__(self, kingName: str):
        self.edges = defaultdict(list)
        self.dead = set()
        self.king = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.edges[parentName].append(childName)

    def death(self, name: str) -> None:
        self.dead.add(name)

    def getInheritanceOrder(self) -> List[str]:
        res = list()
        def p(name: str) -> None:
            if name not in self.dead:
                res.append(name)
            if name in self.edges:
                for childName in self.edges[name]:
                    p(childName)
        p(self.king)
        return res

# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()