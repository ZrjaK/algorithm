package Solution

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

type STNode struct {
	left  *STNode
	right *STNode
	val   int64
	add   int64
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

func (st *SegmentTree) add(node *STNode, l, r, start, end int, x int64) {
	if l == start && r == end {
		node.add += x
		return
	}
	st.pushdown(node)
	mid := (l + r) >> 1
	if end <= mid {
		st.add(node.left, l, mid, start, end, x)
	} else if start > mid {
		st.add(node.right, mid+1, r, start, end, x)
	} else {
		st.add(node.left, l, mid, start, mid, x)
		st.add(node.right, mid+1, r, mid+1, end, x)
	}
	st.pushup(node, mid-l+1, r-mid)
}

func (st *SegmentTree) query(node *STNode, l, r, start, end int) (res int64) {
	if l == start && r == end {
		return node.val + node.add*int64(r-l+1)
	}
	st.pushdown(node)
	mid := (l + r) >> 1
	if end <= mid {
		res = st.query(node.left, l, mid, start, end)
	} else if start > mid {
		res = st.query(node.right, mid+1, r, start, end)
	} else {
		res = st.query(node.left, l, mid, start, mid) +
			st.query(node.right, mid+1, r, mid+1, end)
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
	if node.add > 0 {
		node.left.add += node.add
		node.right.add += node.add
		node.add = 0
	}
}

func (st *SegmentTree) pushup(node *STNode, ln, rn int) {
	node.val = node.left.val + node.right.val + node.left.add*int64(ln) + node.right.add*int64(rn)
}

func main() {
	in := bufio.NewReader(os.Stdin)
	out := bufio.NewWriter(os.Stdout)
	defer out.Flush()
	var n, m int
	fmt.Fscanln(in, &n, &m)
	st := NewSegmentTree()
	var a int64
	for i := 1; i <= n; i++ {
		fmt.Fscan(in, &a)
		st.add(st.root, 1, n, i, i, a)
	}
	for ; m > 0; m-- {
		var q, w, e, r int
		fmt.Fscan(in, &q)
		if q == 1 {
			fmt.Fscan(in, &w, &e, &r)
			st.add(st.root, 1, n, w, e, int64(r))
		} else {
			fmt.Fscan(in, &w, &e)
			out.WriteString(strconv.Itoa(int(st.query(st.root, 1, n, w, e))) + "\n")
		}
	}
}
