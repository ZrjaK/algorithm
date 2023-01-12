# 题目：面试题 16.25.LRU 缓存
# 难度：MEDIUM
# 最后提交：2022-12-11 19:46:05 +0800 CST
# 语言：python3
# 作者：ZrjaK

class LRUCache:

    def __init__(self, capacity: int):
        self.q = DoublyLinkedList()
        self.d = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key in self.d:
            node = self.d[key]
            self.d[key] = self.q.insert_last(self.q.delete_node(node).val)
            return self.d[key].val[1]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.d:
            node = self.d[key]
            self.q.delete_node(node)
        self.d[key] = self.q.insert_last((key, value))
        if len(self.q) > self.capacity:
            node = self.q.delete_first()
            del self.d[node.val[0]]
        


class DoublyLinkedList:
    """双端链表"""

    class _Node:
        __slots__ = "val", "prev", "next"

        def __init__(self, val, prev, next):
            self.val = val
            self.prev = prev
            self.next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header.next = self._trailer
        self._trailer.prev = self._header
        self._size = 0

    def __len__(self):
        return self._size

    def __bool__(self):
        return self._size > 0

    def first(self):
        if not self:
            raise KeyError("empty deque")
        return self._header.next

    def last(self):
        if not self:
            raise KeyError("empty deque")
        return self._trailer.prev

    def _insert_between(self, val, before, after):
        newest = self._Node(val, before, after)
        before.next = newest
        after.prev = newest
        self._size += 1
        return newest

    def delete_node(self, node):
        before = node.prev
        after = node.next
        before.next = after
        after.prev = before
        self._size -= 1
        return node

    def insert_first(self, val):
        return self._insert_between(val, self._header, self._header.next)

    def insert_last(self, val):
        return self._insert_between(val, self._trailer.prev, self._trailer)

    def delete_first(self):
        if not self:
            raise KeyError("empty deque")
        return self.delete_node(self._header.next)

    def delete_last(self):
        if not self:
            raise KeyError("empty deque")
        return self.delete_node(self._trailer.prev)

    def __repr__(self):
        ans = []
        node = self._header.next
        while node.next:
            ans.append(str(node.val))
            node = node.next
        return "deque:" + "<->".join(ans)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)