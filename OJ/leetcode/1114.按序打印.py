# 题目：1114.按序打印
# 难度：EASY
# 最后提交：2021-11-06 16:22:40 +0800 CST
# 语言：python3
# 作者：ZrjaK

from threading import *
class Foo:
    def __init__(self):
        self.s1=Semaphore(1)
        self.s2=Semaphore(0)
        self.s3=Semaphore(0)


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        self.s1.acquire()
        printFirst()
        self.s2.release()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        self.s2.acquire()
        printSecond()
        self.s3.release()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        self.s3.acquire()
        printThird()