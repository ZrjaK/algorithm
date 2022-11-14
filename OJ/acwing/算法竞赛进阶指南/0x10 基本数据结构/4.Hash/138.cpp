#include <bits/stdc++.h>
using namespace std;
#define ll long long
// #define ll __int128
#define ld long double
#define ui unsigned int
#define ull unsigned long long
#define pii pair<int, int>
#define pll pair<ll, ll>
#define pdd pair<ld, ld>
#define vi vector<int>
#define vvi vector<vector<int> >
#define vll vector<ll>
#define vvll vector<vector<ll> >
#define lb lower_bound
#define ub upper_bound
#define pb push_back
#define pf push_front
#define ppf pop_front
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fi first
#define se second
#define rep(i, a, b) for(ll i = a; i < b; ++i)
#define per(i, a, b) for(ll i = a; i > b; --i)
#define each(x, v) for(auto& x: v)
#define len(x) x.size()
#define elif else if
#define all(x) begin(x), end(x)
#define mst(x, a) memset(x, a, sizeof(x))
#ifndef lowbit
#define lowbit(x) (x & (-x))
#endif
#define bitcnt(x) (__builtin_popcountll(x))
#define _up(x) (int)ceil(1.0*x)
#define _down(x) (int)floor(1.0*x)
#define endl "\n"
template <class T>
using pq = priority_queue<T>;
template <class T>
using pqg = priority_queue<T, vector<T>, greater<T> >;
const __int128 ONE = 1;
ll gcd(ll x,ll y) {
	if(!x) return y;
	if(!y) return x;
	int t = __builtin_ctzll(x | y);
	x >>= __builtin_ctzll(x);
	do {
		y >>= __builtin_ctzll(y);
		if(x > y) swap(x, y);
		y -= x;
	} while(y);
	return x<<t;
}
ll lcm(ll x, ll y) { return x * y / gcd(x, y); }
ll max(ll x, ll y) { return x > y ? x : y; }
ll min(ll x, ll y) { return x < y ? x : y; }
ll Mod(ll x, int mod) { return (x % mod + mod) % mod; }
ll pow(ll x, ll y, ll mod){
	ll res = 1, cur = x;
	while (y) {
		if (y & 1)	res = res * cur % mod;
		cur = ONE * cur * cur % mod;
		y >>= 1;
	}
	return res % mod;
}
ll probabilityMod(ll x, ll y, ll mod) {
	return x * pow(y, mod-2, mod) % mod;
}
const ll LINF = 0x1fffffffffffffff;
const ll MINF = 0x7fffffffffff;
const int INF = 0x3fffffff;
const int MOD = 1000000007;
const int MODD = 998244353;
const int N = 1e6 + 10;


template<typename Val, typename Compare = std::less<Val>, int BlockSize = 10>
class DirectRMQ {
public:
	typedef int Index;	//今のところ大きくともintを仮定している(queryとか)
	typedef char InBlockIndex;
	typedef InBlockIndex(*BlockTypeRef)[BlockSize];

	DirectRMQ(Compare comp_ = Compare()) :
		blockTypes(0), innerBlockTable(0), sparseTable(0) {
		comp = comp_;
		calcBallotNumbers();
		buildInnerBlockTable();
	}
	~DirectRMQ() {
		delete[] innerBlockTable;
		delete[] blockTypes; delete[] sparseTable;
	}

	void build(const Val *a, Index n) {
		blocks = (n + BlockSize - 1) / BlockSize;
		stHeight = 0; while(1 << stHeight < blocks) ++ stHeight;
		delete[] blockTypes; delete[] sparseTable;

		blockTypes = new BlockTypeRef[blocks];
		calcBlockTypes(a, n);
		buildInnerBlockTable(a, n);
		sparseTable = new Index[blocks * stHeight];
		buildSparseTable(a);
	}

	//[l,r]の閉区間
	Index query(const Val *a, Index l, Index r) const {
		Index x = l / BlockSize, y = r / BlockSize, z = y - x;
		if(z == 0) return x * BlockSize + blockTypes[x][l % BlockSize][r % BlockSize];
		if(z == 1) return assumeleft_minIndex(a,
			x * BlockSize + blockTypes[x][l % BlockSize][BlockSize - 1],
			y * BlockSize + blockTypes[y][0][r % BlockSize]);
		z -= 2;
		Index k = 0, s;
		s = ((z & 0xffff0000) != 0) << 4; z >>= s; k |= s;
		s = ((z & 0x0000ff00) != 0) << 3; z >>= s; k |= s;
		s = ((z & 0x000000f0) != 0) << 2; z >>= s; k |= s;
		s = ((z & 0x0000000c) != 0) << 1; z >>= s; k |= s;
		s = ((z & 0x00000002) != 0) << 0; z >>= s; k |= s;
		return assumeleft_minIndex(a
			, assumeleft_minIndex(a,
				x * BlockSize + blockTypes[x][l % BlockSize][BlockSize - 1],
				sparseTable[x + 1 + blocks * k])
			, assumeleft_minIndex(a,
				sparseTable[y + blocks * k - (1 << k)],
				y * BlockSize + blockTypes[y][0][r % BlockSize])
			);
	}

	Val queryVal(const Val *a, Index l, Index r) const {
		Index x = l / BlockSize, y = r / BlockSize, z = y - x;
		if(z == 0) return a[x * BlockSize + blockTypes[x][l % BlockSize][r % BlockSize]];
		Val edge = minVal(
			a[x * BlockSize + blockTypes[x][l % BlockSize][BlockSize - 1]],
			a[y * BlockSize + blockTypes[y][0][r % BlockSize]]);
		if(z == 1) return edge;
		z -= 2;
		Index k = 0, s;
		s = ((z & 0xffff0000) != 0) << 4; z >>= s; k |= s;
		s = ((z & 0x0000ff00) != 0) << 3; z >>= s; k |= s;
		s = ((z & 0x000000f0) != 0) << 2; z >>= s; k |= s;
		s = ((z & 0x0000000c) != 0) << 1; z >>= s; k |= s;
		s = ((z & 0x00000002) != 0) << 0; z >>= s; k |= s;
		return minVal(edge, minVal(
			a[sparseTable[x + 1 + blocks * k]],
			a[sparseTable[y + blocks * k - (1 << k)]]));
	}
private:
	Compare comp;

	int ballotNumbers[BlockSize + 1][BlockSize + 1];
	InBlockIndex(*innerBlockTable)[BlockSize][BlockSize];

	Index blocks;
	int stHeight;
	BlockTypeRef *blockTypes;
	Index *sparseTable;

	inline Index minIndex(const Val *a, Index x, Index y) const {
		return comp(a[x], a[y]) || (a[x] == a[y] && x < y) ? x : y;
	}
	inline Index assumeleft_minIndex(const Val *a, Index x, Index y) const {
		return comp(a[y], a[x]) ? y : x;
	}

	inline Val minVal(Val x, Val y) const {
		return comp(y, x) ? y : x;
	}

	void buildSparseTable(const Val *a) {
		Index *b = sparseTable;
		if(stHeight) for(Index i = 0; i < blocks; i ++)
			b[i] = i * BlockSize + blockTypes[i][0][BlockSize - 1];
		for(Index t = 1; t * 2 < blocks; t *= 2) {
			std::memcpy(b + blocks, b, blocks * sizeof(Index));
			b += blocks;
			for(Index i = 0; i < blocks - t; ++ i)
				b[i] = assumeleft_minIndex(a, b[i], b[i + t]);
		}
	}

	void buildInnerBlockTable(const Val *a, Index n) {
		for(Index i = 0; i < blocks; i ++) {
			BlockTypeRef table = blockTypes[i];
			if(table[0][0] != -1) continue;
			const Val *p = getBlock(a, n, i);
			for(InBlockIndex left = 0; left < BlockSize; left ++) {
				Val minV = p[left];
				InBlockIndex minI = left;
				for(InBlockIndex right = left; right < BlockSize; right ++) {
					if(comp(p[right], minV)) {
						minV = p[right];
						minI = right;
					}
					table[left][right] = minI;
				}
			}
		}
	}

	//端っこのブロック用に関数内staticなテンポラリ配列を返す
	const Val *getBlock(const Val *a, Index n, Index i) {
		Index offset = i * BlockSize;
		if(offset + BlockSize <= n)
			return a + offset;
		else {
			static Val tmp_a[BlockSize];
			std::copy(a + offset, a + n, tmp_a);
			Val maxVal = Val();
			for(Index j = i; j < n; j ++)	//iでなくoffsetでは？(動作には問題ないし計算量もほとんど変わらないけれど…)(バグるのが嫌なので(今まで動いていたので)直すのは後にする)
				if(comp(maxVal, a[j])) maxVal = a[j];
			std::fill(tmp_a + (n - offset), tmp_a + BlockSize, maxVal);
			return tmp_a;
		}
	}

	void calcBlockTypes(const Val *a, Index n) {
		Val tmp_rp[BlockSize + 1];
		for(Index i = 0; i < blocks; i ++)
			blockTypes[i] = calcBlockType(getBlock(a, n, i), tmp_rp);
	}

	BlockTypeRef calcBlockType(const Val *a, Val *rp) {
		int q = BlockSize, N = 0;
		for(int i = 0; i < BlockSize; i ++) {
			while(q + i - BlockSize > 0 && comp(a[i], rp[q + i - BlockSize])) {
				N += ballotNumbers[BlockSize - i - 1][q];
				q --;
			}
			rp[q + i + 1 - BlockSize] = a[i];
		}
		return innerBlockTable[N];
	}

	void calcBallotNumbers() {
		for(int p = 0; p <= BlockSize; p ++) {
			for(int q = 0; q <= BlockSize; q ++) {
				if(p == 0 && q == 0)
					ballotNumbers[p][q] = 1;
				else if(p <= q)
					ballotNumbers[p][q] =
					(q ? ballotNumbers[p][q - 1] : 0) +
					(p ? ballotNumbers[p - 1][q] : 0);
				else
					ballotNumbers[p][q] = 0;
			}
		}
	}

	void buildInnerBlockTable() {
		int numberOfTrees = ballotNumbers[BlockSize][BlockSize];
		innerBlockTable = new InBlockIndex[numberOfTrees][BlockSize][BlockSize];
		for(int i = 0; i < numberOfTrees; i ++)
			innerBlockTable[i][0][0] = -1;
	}
};

class SuffixArray {
public:
	typedef char Alpha;
	typedef int Index;

	void build(const Alpha *str, Index n, int AlphaSize);
	void build(const Alpha *str, Index n);
	void buildAll(const Alpha *str, Index n);
	inline Index getKThSuffix(Index k) const { return suffixArray[k]; }
	inline Index length() const { return static_cast<Index>(suffixArray.size() - 1); }
	std::vector<Index> suffixArray;
	template<typename AlphaT> void sa_is(const AlphaT *str, Index n, int AlphaSize, Index *sa, std::vector<Index> &bucketOffsets);
	template<typename AlphaT> void inducedSort(const AlphaT *str, Index n, int AlphaSize, const std::vector<bool> &types, Index *sa, std::vector<Index> &bucketOffsets);
	template<typename AlphaT> void countAlphabets(const AlphaT *str, Index n, int AlphaSize, std::vector<Index> &bucketOffsets, bool b = false);
	template<typename AlphaT> void getBucketOffsets(const AlphaT *str, Index n, bool dir, int AlphaSize, std::vector<Index> &bucketOffsets);
	void buildInverseSuffixArray();
	std::vector<Index> inverseSuffixArray;
	void computeLCPArray(const Alpha *str);
	std::vector<Index> lcpArray;
	typedef DirectRMQ<Index> LCPArrayRMQ;
	LCPArrayRMQ lcpArrayRMQ;
	void preprocessLCPArrayRMQ() {
		lcpArrayRMQ.build(&lcpArray[0], length() + 1);
	}
	Index computeLCP(Index i, Index j) const;
};

void SuffixArray::build(const Alpha *str, Index n, int AlphaSize) {
	suffixArray.resize(n + 1);
	if(n == 0) suffixArray[0] = 0;
	else {
		//I = sizeof(Index) * CHAR_BITS として
		//suffixArray + bucketOffsets + types + 関数ローカル変数
		//= n*I + max(AlphaSize, n/2)*I + 2*n + O(log n) bits
		//I = 4 * 32でAlphaSizeが十分小さいとすると:
		//(6+1/16) * n + O(log n) bytes
		std::vector<Index> bucketOffsets(std::max(AlphaSize, (n + 1) / 2) + 1);
		sa_is<Alpha>(str, n, AlphaSize, &suffixArray[0], bucketOffsets);
	}
}

void SuffixArray::build(const Alpha *str, Index n) {
	Alpha maxElem = *std::max_element(str, str + n);
	assert(maxElem + 0 < std::numeric_limits<int>::max());
	build(str, n, (int)(maxElem + 1));
}

void SuffixArray::buildAll(const Alpha *str, Index n) {
	build(str, n);
	buildInverseSuffixArray();
	computeLCPArray(str);
	preprocessLCPArrayRMQ();
}

//strは[0,n)が有効で番兵は含まれない。saは[0,n]が有効
template<typename AlphaT>
void SuffixArray::sa_is(const AlphaT *str, Index n, int AlphaSize, Index *sa, std::vector<Index> &bucketOffsets) {
	std::vector<bool> types(n + 1);
	types[n - 1] = 0; types[n] = 1;
	for(Index i = n - 2; i >= 0; i --)
		types[i] = str[i] < str[i + 1] || (str[i] == str[i + 1] && types[i + 1]);

	countAlphabets(str, n, AlphaSize, bucketOffsets);
	getBucketOffsets(str, n, true, AlphaSize, bucketOffsets);
	std::fill(sa, sa + n + 1, -1);
	for(Index i = 1; i < n; i ++)
		if(types[i] && !types[i - 1]) sa[-- bucketOffsets[(int)str[i]]] = i;
	sa[0] = n;
	inducedSort(str, n, AlphaSize, types, sa, bucketOffsets);

	Index n1 = 0;
	for(Index i = 0; i <= n; i ++) {
		Index j = sa[i];
		if(j > 0 && types[j] && !types[j - 1]) sa[n1 ++] = j;
	}

	//LMS substringsを番号付けする。sa[0..n1-1]にソートされている。
	//メモリのためにsaの右半分をバッファに利用する。
	//さらにそこでposの順序で整数ソートすることを同時に行う。
	//ここでLMS substringが連続して現れないことやLMS substringの数がn/2以下であることを利用してなんとか1つの配列でやる
	Index *buffer = sa + n1;
	std::fill(buffer, sa + n + 1, -1);
	Index uniqueLMSCount = 0, prevPos = -1;
	assert(sa[0] == n);
	buffer[sa[0] / 2] = uniqueLMSCount ++;	//'$'
	for(Index i = 1; i < n1; i ++) {
		Index pos = sa[i]; bool diff = false;
		if(prevPos == -1) diff = true;
		else for(Index j = pos, k = prevPos; ; j ++, k ++) {
			if(str[j] != str[k] || types[j] != types[k]) {
				diff = true;
				break;
			} else if(j != pos && ((types[j] && !types[j - 1]) || (types[k] && !types[k - 1])))
				break;
		}
		if(diff) {
			uniqueLMSCount ++;
			prevPos = pos;
		}
		buffer[pos / 2] = uniqueLMSCount - 1;
	}
	for(Index i = n, j = n; i >= n1; i --)
		if(sa[i] >= 0) sa[j --] = sa[i];

	Index *sa1 = sa, *s1 = sa + n + 1 - n1;
	if(uniqueLMSCount == n1)
		for(Index i = 0; i < n1; i ++) sa1[s1[i]] = i;
	else
		sa_is<Index>(s1, n1 - 1, uniqueLMSCount, sa1, bucketOffsets);

	countAlphabets(str, n, AlphaSize, bucketOffsets);
	getBucketOffsets(str, n, true, AlphaSize, bucketOffsets);
	for(Index i = 1, j = 0; i <= n; i ++)
		if(types[i] && !types[i - 1]) s1[j ++] = i;
	for(Index i = 0; i < n1; i ++) sa1[i] = s1[sa1[i]];
	std::fill(sa + n1, sa + n + 1, -1);
	for(Index i = n1 - 1; i >= 1; i --) {
		Index j = sa[i]; sa[i] = -1;
		sa[-- bucketOffsets[(int)str[j]]] = j;
	}
	inducedSort(str, n, AlphaSize, types, sa, bucketOffsets);
}

template<typename AlphaT>
void SuffixArray::inducedSort(const AlphaT *str, Index n, int AlphaSize, const std::vector<bool> &types, Index *sa, std::vector<Index> &bucketOffsets) {
	getBucketOffsets(str, n, false, AlphaSize, bucketOffsets);
	for(Index i = 0; i < n; i ++) {
		Index j = sa[i] - 1;
		if(j >= 0 && !types[j]) sa[bucketOffsets[(int)str[j]] ++] = j;
	}

	getBucketOffsets(str, n, true, AlphaSize, bucketOffsets);
	for(Index i = n; i >= 1; i --) {
		Index j = sa[i] - 1;
		if(j >= 0 && types[j]) sa[-- bucketOffsets[(int)str[j]]] = j;
	}
}

template<typename AlphaT>
void SuffixArray::countAlphabets(const AlphaT *str, Index n, int AlphaSize, std::vector<Index> &bucketOffsets, bool b) {
	if(b || (int)bucketOffsets.size() / 2 >= AlphaSize) {
		std::vector<Index>::iterator alphabetCounts =
			b ? bucketOffsets.begin() : bucketOffsets.begin() + AlphaSize;
		std::fill(alphabetCounts, alphabetCounts + AlphaSize, 0);
		for(Index i = 0; i < n; i ++)
			alphabetCounts[(int)str[i]] ++;
	}
}

template<typename AlphaT>
void SuffixArray::getBucketOffsets(const AlphaT *str, Index n, bool dir, int AlphaSize, std::vector<Index> &bucketOffsets) {
	//AlphaSizeが大きい場合にはbucketOffset求めるたびにalphabetを数えてメモリ量を少なくし、
	//AlphaSizeが小さい場合にはbucketOffsetをalphabetCountsと別の場所に置くことにする。
	std::vector<Index>::iterator alphabetCounts;
	if((int)bucketOffsets.size() / 2 < AlphaSize) {
		countAlphabets(str, n, AlphaSize, bucketOffsets, true);
		alphabetCounts = bucketOffsets.begin();
	} else alphabetCounts = bucketOffsets.begin() + AlphaSize;
	Index cumsum = 1;	//'$'の分
	if(dir) {
		for(int i = 0; i < AlphaSize; i ++) {
			cumsum += alphabetCounts[i];
			bucketOffsets[i] = cumsum;
		}
	} else {
		for(int i = 0; i < AlphaSize; i ++) {
			Index x = alphabetCounts[i];
			bucketOffsets[i] = cumsum;
			cumsum += x;
		}
	}
}

void SuffixArray::buildInverseSuffixArray() {
	Index n = length();
	inverseSuffixArray.resize(n + 1);
	for(Index i = 0; i <= n; i ++)
		inverseSuffixArray[suffixArray[i]] = i;
}

void SuffixArray::computeLCPArray(const Alpha *str) {
	int n = length();
	lcpArray.resize(n + 2);
	Index h = 0;
	for(Index i = 0; i < n; i ++) {
		Index pos = inverseSuffixArray[i];
		Index j = suffixArray[pos - 1];
		Index hbound = std::min(n - j, n - i);
		for(Index k = 0; h < hbound && str[i + h] == str[j + h]; ++ h);
		lcpArray[pos - 1] = h;
		if(h > 0) -- h;
	}
	lcpArray[n] = lcpArray[n + 1] = 0;
}

SuffixArray::Index SuffixArray::computeLCP(Index i, Index j) const {
	Index n = length();
	if(i == j) return n - i;
	Index x = inverseSuffixArray[i], y = inverseSuffixArray[j];
	if(x > y) std::swap(x, y);
	return lcpArrayRMQ.queryVal(&lcpArray[0], x, y - 1);
}

void solve() {
	string s;
	cin >> s;
	SuffixArray sa;
	sa.buildAll(s.c_str(), len(s));
	int m, l1, r1, l2, r2;
	cin >> m;
	rep(i, 0, m) {
		cin >> l1 >> r1 >> l2 >> r2;
		if(sa.computeLCP(l1, l2) >= r1-l1) cout << "Yes" << endl;
		else cout << "No" << endl;
	}


}

signed main() {
	ios::sync_with_stdio(0);
	cin.tie(0);
	cout.tie(0);
    int t = 1;
	// cin >> t;
    while (t--) {
        solve();
    }
	return 0;
}
