# 题目：690.员工的重要性
# 难度：MEDIUM
# 最后提交：2021-10-23 14:30:38 +0800 CST
# 语言：python3
# 作者：ZrjaK

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        res = 0
        hashmap = dict()
        
        for employee in employees:
            hashmap[employee.id] = [employee.importance, employee.subordinates]
        
        queue = [id]
        while(queue):
            next_queue = []
            for item in queue:
                res += hashmap[item][0]
                next_queue += hashmap[item][1] #把下属列表加入下一次的queue                
            queue = next_queue[:]
            
        return res
