ll fac[N];
ll inv[N];

void init(ll mod) {
    fac[0] = 1;
    for (int i = 1; i < N; i++) {
        fac[i] = (fac[i - 1] * i) % mod;
    }
    inv[0] = inv[1] = 1;
    for (int i = 2; i < N; i++) {
        inv[i] = (ll) (mod - mod / i) * inv[mod % i] % mod;
    }
    for (int i = 1; i < N; i++) {
        inv[i] = (inv[i - 1] * inv[i]) % mod;
    }
}

ll C(ll n, ll m, ll mod) {
    return n < m ? 0 : fac[n] * inv[m] % mod * inv[n - m] % mod;
}

ll P(ll n, ll m, ll mod) {
    return n < m ? 0 : fac[n] * inv[n - m] % mod;
}

ll lucas(ll n, ll m, ll mod)
{
    if(n < m) return 0;
    else if(n < mod) return C(n, m, mod);
    else return lucas(n / mod, m / mod, mod) * lucas(n % mod, m % mod, mod) % mod;
}
