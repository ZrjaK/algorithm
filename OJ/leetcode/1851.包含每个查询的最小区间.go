// 题目：1851.包含每个查询的最小区间
// 难度：HARD
// 最后提交：2022-09-27 15:34:57 +0800 CST
// 语言：golang
// 作者：ZrjaK

func minInterval(intervals [][]int, queries []int) []int {
    st := NewSegmentTree()
    for _, i := range intervals {
        st.assign(st.root, 1, 10000000, i[0], i[1], int64(i[1]-i[0]+1))
    }
    ans := []int{}
    for _, i := range queries {
        t := int(st.query(st.root, 1, 10000000, i, i))
        if t > 10000000 {
            t = -1
        }
        ans = append(ans, t)
    }
    return ans
}

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
		node.lazy = min(node.lazy+node.val, x)
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
	// st.pushup(node, mid-l+1, r-mid)
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
        node.left.lazy = 1000000000
	}
	if node.right == nil {
		node.right = new(STNode)
        node.right.lazy = 1000000000
	}
	if node.lazy > 0 {
		node.left.lazy = min(node.left.lazy, node.lazy)
		node.right.lazy = min(node.right.lazy, node.lazy)
		// node.lazy = 0
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
