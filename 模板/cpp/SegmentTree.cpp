class SegmentTree {
public:
	struct STNode {
		STNode () : left(nullptr), right(nullptr), val(0), maxval(0), minval(0), lazy(0), mlazy(LINF) {}
		STNode* left;
		STNode* right;
		long long val;
		long long maxval;
		long long minval;
		long long lazy;
		long long mlazy;
	};
	STNode* root;
    int L, R;
	SegmentTree(int _L, int _R) : L(_L), R(_R) { root = new STNode(); }
	~SegmentTree() {}

    void assign(int start, int end, long long x) {
        assert(L <= start && start <= end && end <= R);
        _assign(root, L, R, start, end, x);
    }

	void _assign(STNode* node, int l, int r, int start, int end, long long x) {
		if (l == start && r == end) {
			node->val = 0;
			node->maxval = 0;
			node->minval = 0;
			node->lazy = 0;
			node->mlazy = x;
			return;
		}
		pushdown(node);
		int mid = l+r>>1;
		if (end <= mid) {
			_assign(node->left, l, mid, start, end, x);
		} else if (start > mid) {
			_assign(node->right, mid+1, r, start, end, x);
		} else {
			_assign(node->left, l, mid, start, mid , x);
			_assign(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

    void add(int start, int end, long long x) {
        assert(L <= start && start <= end && end <= R);
        _add(root, L, R, start, end, x);
    }

	void _add(STNode* node, int l, int r, int start, int end, long long x){
		if (l == start && r == end) {
			node->lazy += x;
			return;
		}
		pushdown(node);
		int mid = l+r>>1;
		if (end <= mid) {
			_add(node->left, l, mid, start, end, x);
		} else if (start > mid) {
			_add(node->right, mid+1, r, start, end, x);
		} else {
			_add(node->left, l, mid, start, mid , x);
			_add(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

    long long querySum(int start, int end) {
        assert(L <= start && start <= end && end <= R);
        return _querySum(root, L, R, start, end);
    }

	long long _querySum(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->val + node->lazy * (r-l+1) + \
				(node->mlazy == LINF ? 0 : node->mlazy * (r-l+1));
		}
		pushdown(node);
		int mid = l+r>>1;
		long long res;
		if (end <= mid) {
			res = _querySum(node->left, l, mid, start, end);
		} else if (start > mid) {
			res = _querySum(node->right, mid+1, r, start, end);
		} else {
			res = _querySum(node->left, l, mid, start, mid) +
			_querySum(node->right, mid+1, r, mid+1, end);
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

    long long queryMax(int start, int end) {
        assert(L <= start && start <= end && end <= R);
        return _queryMax(root, L, R, start, end);
    }

	long long _queryMax(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->maxval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		long long res;
		if (end <= mid) {
			res = _queryMax(node->left, l, mid, start, end);
		} else if (start > mid) {
			res = _queryMax(node->right, mid+1, r, start, end);
		} else {
			res = max(_queryMax(node->left, l, mid, start, mid),
			_queryMax(node->right, mid+1, r, mid+1, end));
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

    long long queryMin(int start, int end) {
        assert(L <= start && start <= end && end <= R);
        return _queryMin(root, L, R, start, end);
    }

	long long _queryMin(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->minval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		long long res;
		if (end <= mid) {
			res = _queryMin(node->left, l, mid, start, end);
		} else if (start > mid) {
			res = _queryMin(node->right, mid+1, r, start, end);
		} else {
			res = min(_queryMin(node->left, l, mid, start, mid),
			_queryMin(node->right, mid+1, r, mid+1, end));
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

	void pushdown(STNode* node) {
		if (node->left == nullptr) {
			node->left = new STNode();
		}
		if (node->right == nullptr) {
			node->right = new STNode();
		}
		if (node->mlazy != LINF) {
			node->left->lazy = 0;
			node->left->val = 0;
			node->left->maxval = 0;
			node->left->minval = 0;
		
			node->right->lazy = 0;
			node->right->val = 0;
			node->right->maxval = 0;
			node->right->minval = 0;
			
			node->left->mlazy = node->mlazy;
			node->right->mlazy = node->mlazy;
			node->mlazy = LINF;
		}
		if (node->lazy) {
			node->left->lazy += node->lazy;
			node->right->lazy += node->lazy;
			node->lazy = 0;
		}
	}

	void pushup(STNode* node, int ln, int rn) {
		node->val = node->left->val + node->left->lazy * ln + \
					(node->left->mlazy == LINF ? 0 : node->left->mlazy * ln) + \ 
					node->right->val + node->right->lazy * rn + \
					(node->right->mlazy == LINF ? 0 : node->right->mlazy * rn);

		node->maxval = max(node->left->maxval + node->left->lazy + \
						(node->left->mlazy == LINF ? 0 : node->left->mlazy),
						node->right->maxval + node->right->lazy + \
						(node->right->mlazy == LINF ? 0 : node->right->mlazy));

		node->minval = min(node->left->minval + node->left->lazy + \
						(node->left->mlazy == LINF ? 0 : node->left->mlazy),
						node->right->minval + node->right->lazy + \
						(node->right->mlazy == LINF ? 0 : node->right->mlazy));

	}
};