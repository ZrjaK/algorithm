// 题目：981.基于时间的键值存储
// 难度：MEDIUM
// 最后提交：2022-05-03 11:08:13 +0800 CST
// 语言：cpp
// 作者：ZrjaK

class TimeMap {
public:
    /** Initialize your data structure here. */
    unordered_map<string, map<int, string, greater<int>>> kv;
    
    TimeMap() {
        kv.clear();
    }
    
    void set(string key, string value, int timestamp) {
        kv[key][timestamp] = value;
    }
    
    string get(string key, int timestamp) {
        auto& values = kv[key];
        return values.lower_bound(timestamp)->second;
    }
};

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap* obj = new TimeMap();
 * obj->set(key,value,timestamp);
 * string param_2 = obj->get(key,timestamp);
 */