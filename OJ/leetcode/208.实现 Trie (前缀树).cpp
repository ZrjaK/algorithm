// 题目：208.实现 Trie (前缀树)
// 难度：MEDIUM
// 最后提交：2023-02-07 21:36:29 +0800 CST
// 语言：cpp
// 作者：ZrjaK

#include <ext/pb_ds/assoc_container.hpp>
using namespace __gnu_pbds;
#include <ext/pb_ds/trie_policy.hpp>

class Trie {
public:
    trie<string, null_type, trie_string_access_traits<>, pat_trie_tag, trie_prefix_search_node_update> t;
    Trie() {
        
    }
    
    void insert(string word) {
        t.insert(word);
    }
    
    bool search(string word) {
        return t.find(word) != t.end();
    }
    
    bool startsWith(string prefix) {
        auto [start, end] = t.prefix_range(prefix);
        return start != end;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */