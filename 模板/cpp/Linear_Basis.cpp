const int logN = 64;
struct Linear_Basis {
	ll b[logN];
    vll d;
    ll zero = 0;
	// 初始化
	Linear_Basis() {
		memset(b, 0, sizeof b);
	}

	// 插入 x
	bool insert(ll x) {
		for (int i = logN - 1; i >= 0; i--) {
			if (x >> i & 1) {
				if (!b[i]) {
					b[i] = x;
					return true;
				} else {
					x ^= b[i];
				}
			}
		}
        if (!x) zero = 1;
		return false;
	}

	// x 与线性基异或的最大值，x=0 时表示线性基能表示出的最大值
	ll qrymx(ll x = 0) {
		for (int i = logN - 1; i >= 0; i--) {
			x = max(x, x ^ b[i]);
		}
		return x;
	}

	void join(Linear_Basis t) {
		for (int i = logN - 1; i >= 0; i--) {
			insert(t.b[i]);
		}
	}

    void rebuild() {
        d.clear();
        for (int i = logN - 1; i >= 0; i--)
            for (int j = i - 1; j >= 0; j--)
                if (b[i] >> j & 1) 
                    b[i] ^= b[j];
        for (int i = 0; i < logN; i++) 
            if (b[i])
                d.emplace_back(b[i]);
    }

    // rebuild before kth
    ll kth(ll k) {
        k -= zero;
        if (k >= (1ll << d.size())) return -1;
        ll ans = 0;
        for (int i = logN - 1; i >= 0; i--)
            if (k >> i & 1) ans ^= d[i];
        return ans;
    }
};