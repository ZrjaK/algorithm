int phi[N], pfact[N];
// int mobious[N];
vi primes;
// vi fact[N];
void init() {
    phi[1] = 1;
    // mobious[1] = 1;
    rep(i, 1, N) {
        if(!phi[i]) {
            primes.pb(i);
            phi[i] = i-1;
            // mobious[i] = -1;
            rep(j, 1, N) {
                if(i * j >= N) break;
                pfact[i*j] = i;
            }
        }
        each(j, primes) {
            if(i * j >= N) break;
            if(i % j == 0) {
                phi[i*j] = phi[i] * j;
                // mobious[i*j] = 0;
                break;
            }
            phi[i*j] = phi[i] * (j - 1);
            // mobious[i*j] = mobious[i] * mobious[j];
        }
        // for(int j = i; j < N; j += i) fact[j].pb(i);
    }
}

map<int, int> getfact(int x) {
    map<int, int> res;
    while(x != 1) res[pfact[x]]++, x /= pfact[x];
    return res;
}

vi factlist(int x) {
    vi res;
    res.clear();
    res.pb(1);
    while(x != 1) {
        int k = pfact[x];
        int c = 0;
        while(x % k == 0) c++, x /= k;
        vi tmp;
        each(i, res) rep(j, 1, c+1) tmp.pb(i * pow(k, j));
        res.insert(res.end(), all(tmp));
    }
    return res;
}
