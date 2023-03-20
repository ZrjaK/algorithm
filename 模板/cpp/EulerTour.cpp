pair<vector<int>, vector<int>> EulerTour(vector<vector<int>>& E, int root = 0) {
    int n = E.size();
    vector<int> IN(n, -1);
    vector<int> OUT(n, 0);
    vector<pair<int, int>> stack = {{root, 1}, {root, 0}};
    int ind = 0;
    while (stack.size()) {
        auto [pos, t] = stack.back();
        stack.pop_back();
        if (!t) {
            IN[pos] = ind++;
            for (auto& npos : E[pos]) if (IN[npos] == -1) {
                stack.emplace_back(pair{npos, 1});
                stack.emplace_back(pair{npos, 0});
            }
        } else OUT[pos] = ind;
    }
    return {IN, OUT};
}