// 题目：面试题 16.02.单词频率
// 难度：MEDIUM
// 最后提交：2022-10-24 21:37:04 +0800 CST
// 语言：cpp
// 作者：ZrjaK

class WordsFrequency {
public:
    unordered_map<string, int> d;
    WordsFrequency(vector<string>& book) {
        d.clear();
        for(auto& i: book) d[i]++;
    }
    
    int get(string word) {
        return d.find(word) != d.end() ? d[word] : 0;
    }
};

/**
 * Your WordsFrequency object will be instantiated and called as such:
 * WordsFrequency* obj = new WordsFrequency(book);
 * int param_1 = obj->get(word);
 */