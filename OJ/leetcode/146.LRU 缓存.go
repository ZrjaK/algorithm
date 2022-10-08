// 题目：146.LRU 缓存
// 难度：MEDIUM
// 最后提交：2022-03-21 20:45:23 +0800 CST
// 语言：golang
// 作者：ZrjaK

import "container/list"

type LRUCache struct {
    m map[int]*list.Element
    queue *list.List
    capacity int
}

type Info struct {
    key int
    value int
}


func Constructor(capacity int) LRUCache {
    t := LRUCache{
        m: map[int]*list.Element{},
        queue: list.New(),
        capacity: capacity,
    }
    return t
}


func (this *LRUCache) Get(key int) int {
    if node, ok := this.m[key]; ok {
        this.m[key] = this.queue.PushBack(this.queue.Remove(node))
        return this.m[key].Value.(Info).value
    }
    return -1
}


func (this *LRUCache) Put(key int, value int)  {
    if node, ok := this.m[key]; ok {
        this.queue.Remove(node)
        this.m[key] = this.queue.PushBack(Info{key:key,value:value})
        return
    }
    this.m[key] = this.queue.PushBack(Info{key:key,value:value})
    if this.queue.Len() > this.capacity {
        delete(this.m, this.queue.Remove(this.queue.Front()).(Info).key)
    }
}


/**
 * Your LRUCache object will be instantiated and called as such:
 * obj := Constructor(capacity);
 * param_1 := obj.Get(key);
 * obj.Put(key,value);
 */