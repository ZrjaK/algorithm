#line 2 "random/base.hpp"

u64 RNG_64() {
  static uint64_t x_
      = uint64_t(chrono::duration_cast<chrono::nanoseconds>(
                     chrono::high_resolution_clock::now().time_since_epoch())
                     .count())
        * 10150724397891781847ULL;
  x_ ^= x_ << 7;
  return x_ ^= x_ >> 9;
}

u64 RNG(u64 lim) { return RNG_64() % lim; }

ll RNG(ll l, ll r) { return l + RNG_64() % (r - l); }
#line 2 "mod/modint61.hpp"

struct modint61 {
  static constexpr u64 mod = (1ULL << 61) - 1;
  u64 val;
  constexpr modint61() : val(0ULL) {}
  constexpr modint61(u32 x) : val(x) {}
  constexpr modint61(u64 x) : val(x % mod) {}
  constexpr modint61(int x) : val((x < 0) ? (x + static_cast<ll>(mod)) : x) {}
  constexpr modint61(ll x)
      : val(((x %= static_cast<ll>(mod)) < 0) ? (x + static_cast<ll>(mod))
                                              : x) {}
  static constexpr u64 get_mod() { return mod; }
  modint61 &operator+=(const modint61 &a) {
    val = ((val += a.val) >= mod) ? (val - mod) : val;
    return *this;
  }
  modint61 &operator-=(const modint61 &a) {
    val = ((val -= a.val) >= mod) ? (val + mod) : val;
    return *this;
  }
  modint61 &operator*=(const modint61 &a) {
    const unsigned __int128 y = static_cast<unsigned __int128>(val) * a.val;
    val = (y >> 61) + (y & mod);
    val = (val >= mod) ? (val - mod) : val;
    return *this;
  }
  modint61 &operator/=(const modint61 &a) { return (*this *= a.inverse()); }
  modint61 operator+(const modint61 &p) const { return modint61(*this) += p; }
  modint61 operator-(const modint61 &p) const { return modint61(*this) -= p; }
  modint61 operator*(const modint61 &p) const { return modint61(*this) *= p; }
  modint61 operator/(const modint61 &p) const { return modint61(*this) /= p; }
  bool operator==(const modint61 &p) const { return val == p.val; }
  bool operator!=(const modint61 &p) const { return val != p.val; }
  modint61 inverse() const {
    ll a = val, b = mod, u = 1, v = 0, t;
    while (b > 0) {
      t = a / b;
      swap(a -= t * b, b), swap(u -= t * v, v);
    }
    return modint61(u);
  }
  modint61 pow(ll n) const {
    assert(n >= 0);
    modint61 ret(1), mul(val);
    while (n > 0) {
      if (n & 1) ret *= mul;
      mul *= mul, n >>= 1;
    }
    return ret;
  }
};

#ifdef FASTIO
void rd(modint61 &x) {
  fastio::rd(x.val);
  assert(0 <= x.val && x.val < modint61::mod);
}

void wt(modint61 x) { fastio::wt(x.val); }
#endif
#line 4 "string/rollinghash.hpp"

struct RollingHash {
  using mint = modint61;
  static constexpr u64 mod = mint::get_mod();
  const mint base;
  vc<mint> power;

  static inline mint generate_base() { return RNG(mod); }

  inline void expand(size_t sz) {
    if (power.size() < sz + 1) {
      int pre_sz = (int)power.size();
      power.resize(sz + 1);
      FOR(i, pre_sz - 1, sz) power[i + 1] = power[i] * base;
    }
  }

  explicit RollingHash(mint base = generate_base()) : base(base), power{1} {}

  template <typename STRING>
  vector<mint> build(const STRING& s) const {
    int sz = s.size();
    vector<mint> hashed(sz + 1, mint(0));
    for (int i = 0; i < sz; i++) { hashed[i + 1] = hashed[i] * base + s[i]; }
    return hashed;
  }

  template <typename STRING>
  mint eval(string& s) {
    mint x = 0;
    for (auto& ch: s) x = base * x + ch;
    return x;
  }

  mint query(const vc<mint>& s, int l, int r) {
    expand(r - l);
    return (s[r] - s[l] * power[r - l]);
  }

  mint combine(mint h1, mint h2, int h2len) {
    expand(h2len);
    return h1 * power[h2len] + h2;
  }

  mint add_char(mint h, int x) { return h * base + mint(x); }

  int lcp(const vc<mint>& a, int l1, int r1, const vc<mint>& b, int l2,
          int r2) {
    int len = min(r1 - l1, r2 - l2);
    int low = 0, high = len + 1;
    while (high - low > 1) {
      int mid = (low + high) / 2;
      if (query(a, l1, l1 + mid) == query(b, l2, l2 + mid))
        low = mid;
      else
        high = mid;
    }
    return low;
  }
};