class SegmentTree {
public:
	struct STNode {
		STNode () : left(nullptr), right(nullptr), val(0), maxval(0), minval(0), lazy(0), mlazy(LINF) {}
		STNode* left;
		STNode* right;
		ll val;
		ll maxval;
		ll minval;
		ll lazy;
		ll mlazy;
	};
	STNode* root;
	SegmentTree() { root = new STNode(); }
	~SegmentTree() {}

	void assign(STNode* node, int l, int r, int start, int end, ll x) {
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
			assign(node->left, l, mid, start, end, x);
		} elif (start > mid) {
			assign(node->right, mid+1, r, start, end, x);
		} else {
			assign(node->left, l, mid, start, mid , x);
			assign(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

	void add(STNode* node, int l, int r, int start, int end, ll x){
		if (l == start && r == end) {
			node->lazy += x;
			return;
		}
		pushdown(node);
		int mid = l+r>>1;
		if (end <= mid) {
			add(node->left, l, mid, start, end, x);
		} elif (start > mid) {
			add(node->right, mid+1, r, start, end, x);
		} else {
			add(node->left, l, mid, start, mid , x);
			add(node->right, mid+1, r, mid+1, end, x);
		}
		pushup(node, mid-l+1, r-mid);
	}

	ll querySum(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->val + node->lazy * (r-l+1) + \
				(node->mlazy == LINF ? 0 : node->mlazy * (r-l+1));
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = querySum(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = querySum(node->right, mid+1, r, start, end);
		} else {
			res = querySum(node->left, l, mid, start, mid) +
			querySum(node->right, mid+1, r, mid+1, end);
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

	ll queryMax(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->maxval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = queryMax(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = queryMax(node->right, mid+1, r, start, end);
		} else {
			res = max(queryMax(node->left, l, mid, start, mid),
			queryMax(node->right, mid+1, r, mid+1, end));
		}
		pushup(node, mid-l+1, r-mid);
		return res;
	}

	ll queryMin(STNode* node, int l, int r, int start, int end) {
		if (l == start && r == end) {
			return node->minval + node->lazy + \
				(node->mlazy == LINF ? 0 : node->mlazy);
		}
		pushdown(node);
		int mid = l+r>>1;
		ll res;
		if (end <= mid) {
			res = queryMin(node->left, l, mid, start, end);
		} elif (start > mid) {
			res = queryMin(node->right, mid+1, r, start, end);
		} else {
			res = min(queryMin(node->left, l, mid, start, mid),
			queryMin(node->right, mid+1, r, mid+1, end));
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
