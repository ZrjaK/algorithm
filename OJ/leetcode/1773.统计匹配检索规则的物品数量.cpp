// 题目：1773.统计匹配检索规则的物品数量
// 难度：EASY
// 最后提交：2022-10-29 00:07:32 +0800 CST
// 语言：cpp
// 作者：ZrjaK

class Solution {
public:
    int countMatches(vector<vector<string>>& items, string ruleKey, string ruleValue) {
        int ans = 0;
        int f;
        if (ruleKey == "type") f = 0;
        if (ruleKey == "color") f = 1;
        if (ruleKey == "name") f = 2;
        for (auto& a: items) if (a[f] == ruleValue) ans++;
        return ans;
    }
};