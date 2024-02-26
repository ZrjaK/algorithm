template<typename T>
tuple<T, T, T> extgcd(T a, T b) {
    if (b == 0) return {a, 1, 0};
    auto [d, p, q] = extgcd(b, a % b);
    T x = q, y = p - q * (a / b);
    return {d, x, y};
}

template<typename T>
T f(T a, T b, T c) {
    // ax+by=cを満たす最小の非負整数yを返す,存在しないなら-1
    T g = gcd(a, b);
    if (c == 0) return 0;
    else if (c % g) return -1;
    else {
        if (g == 1) {
            auto [_, __, y] = extgcd(a, b);
            return ((y * c / g) % a + a) % a;
        } else {
            return f(a / g, b / g, c / g);
        }
    }
}
