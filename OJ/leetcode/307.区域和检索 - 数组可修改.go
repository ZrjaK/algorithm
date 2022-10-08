// 题目：307.区域和检索 - 数组可修改
// 难度：MEDIUM
// 最后提交：2022-08-23 13:30:39 +0800 CST
// 语言：golang
// 作者：ZrjaK

type NumArray struct {
    st *SegmentTree
}


func Constructor(nums []int) NumArray {
    st := NewSegmentTree()
    for i, v := range nums {
        st.add(st.root, 1, 30000, i+1, i+1, int64(v))
    }
    return NumArray{st: st}
}


func (this *NumArray) Update(index int, val int)  {
    v := int64(val) - this.st.query(this.st.root, 1, 30000, index+1, index+1)
    this.st.add(this.st.root, 1, 30000, index+1, index+1, v)
}


func (this *NumArray) SumRange(left int, right int) int {
    return int(this.st.query(this.st.root, 1, 30000, left+1, right+1))
}

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


/**
 * Your NumArray object will be instantiated and called as such:
 * obj := Constructor(nums);
 * obj.Update(index,val);
 * param_2 := obj.SumRange(left,right);
 */