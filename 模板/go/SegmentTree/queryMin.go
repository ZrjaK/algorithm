package Solution

type STNode struct {
	left  *STNode
	right *STNode
	val   int64
	lazy  int64
}

type SegmentTree struct {
	root *STNode
}

func NewSegmentTree() *SegmentTree {
	st := &SegmentTree{
		root: new(STNode),
	}
	return st
}

func (st *SegmentTree) assign(node *STNode, l, r, start, end int, x int64) {
	if l == start && r == end {
		node.lazy = x
		return
	}
	st.pushdown(node)
	mid := (l + r) >> 1
	if end <= mid {
		st.assign(node.left, l, mid, start, end, x)
	} else if start > mid {
		st.assign(node.right, mid+1, r, start, end, x)
	} else {
		st.assign(node.left, l, mid, start, mid, x)
		st.assign(node.right, mid+1, r, mid+1, end, x)
	}
	st.pushup(node, mid-l+1, r-mid)
}

func (st *SegmentTree) query(node *STNode, l, r, start, end int) (res int64) {
	if l == start && r == end {
		return node.val + node.lazy
	}
	st.pushdown(node)
	mid := (l + r) >> 1
	if end <= mid {
		res = st.query(node.left, l, mid, start, end)
	} else if start > mid {
		res = st.query(node.right, mid+1, r, start, end)
	} else {
		res = min(st.query(node.left, l, mid, start, mid),
			st.query(node.right, mid+1, r, mid+1, end))
	}
	st.pushup(node, mid-l+1, r-mid)
	return
}

func (st *SegmentTree) pushdown(node *STNode) {
	if node.left == nil {
		node.left = new(STNode)
	}
	if node.right == nil {
		node.right = new(STNode)
	}
	if node.lazy > 0 {
		node.left.lazy = node.lazy
		node.right.lazy = node.lazy
		node.lazy = 0
	}
}

func (st *SegmentTree) pushup(node *STNode, ln, rn int) {
	node.val = min(node.left.val+node.left.lazy*int64(ln), node.right.val+node.right.lazy*int64(rn))
}

func min(a, b int64) int64 {
	if a < b {
		return a
	}
	return b
}
