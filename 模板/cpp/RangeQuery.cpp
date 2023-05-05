template <class T, T (*func)(T, T)>
struct RangeQuery {
    vector<vector<T>> data;
    RangeQuery(vector<T>& init) {
        data = vector<vector<T>>();
        data.push_back(vector(init));
        int n = init.size();
        for (int i = 1; 2 * i <= n; i <<= 1) {
            auto pre = data.back();
            vector<T> tmp;
            for (int j = 0; j < n - 2 * i + 1; j++) {
                tmp.push_back(func(pre[j], pre[j+i]));
            }
            data.push_back(tmp);
        }
    }

    T query(int start, int stop) {
        int depth = __lg(stop - start);
        return func(data[depth][start], data[depth][stop - (1 << depth)]);
    }
};