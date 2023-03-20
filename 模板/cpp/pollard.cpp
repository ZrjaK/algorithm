bool isprime(ll n) {
	if (n <= 1) return false;
	elif (n == 2) return true;
	elif (n % 2 == 0) return false;
	ll A[7] = {2, 325, 9375, 28178, 450775, 9780504, 1795265022};
	ll s = 0, d = n-1;
	while (d % 2 == 0) s++, d >>= 1;
	each(a, A) {
		if (a % n == 0) return true;
		ll x = pow(a, d, n);
		if (x != 1) {
			bool f = true;
			rep(i, 0, s) {
				if (x == n-1) { f = false; break; }
				x = ONE * x * x % n;
			}
			if (f) return false; 
		}
	}
	return true;
}

ll pollard(ll n) {
	if (n % 2 == 0) return 2;
	if (isprime(n)) return n;
	auto f = [&] (ll x) { return (ONE * x * x % n + 1) % n;};
	ll step = 0;
	while(1) {
		step++;
		ll x = step;
		ll y = f(x);
		while(1) {
			ll p = gcd(y - x + n, n);
			if (p == 0 || p == n) break;
			if (p != 1) return p;
			x = f(x);
			y = f(f(y));
		}
	}
}

vll primefact(ll n) {
	if (n == 1) return vll{};
	ll p = pollard(n);
	if (p == n) { return vll{p}; }
	vll left = primefact(p), right = primefact(n / p);
	left.insert(left.end(), all(right));
	sort(all(left));
	return left;
}
