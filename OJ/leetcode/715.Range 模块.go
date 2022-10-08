// 题目：715.Range 模块
// 难度：HARD
// 最后提交：2022-08-23 13:03:36 +0800 CST
// 语言：golang
// 作者：ZrjaK

type RangeModule struct {
    St *SegmentTree
}

func Constructor() RangeModule {
    return RangeModule{St: NewSegmentTree() }
}


func (this *RangeModule) AddRange(left int, right int)  {
    this.St.Add(this.St.Root, 1, int(1e9), left, right-1, 1)
}


func (this *RangeModule) QueryRange(left int, right int) bool {
    return this.St.Query(this.St.Root, 1, int(1e9), left, right-1) == 1
}


func (this *RangeModule) RemoveRange(left int, right int)  {
    this.St.Add(this.St.Root, 1, int(1e9), left, right-1, 0)
}

type STNode struct {
	Left  *STNode
	Right *STNode
	Val   int64
	Add   int64
}

type SegmentTree struct {
	Root *STNode
}

func NewSegmentTree() *SegmentTree {
	st := &SegmentTree{
		Root: new(STNode),
	}
	return st
}
func (st *SegmentTree) Add(node *STNode, l, r, start, end int, x int64) {
	if l == start && r == end {
        node.Val = x
		node.Add = 1
		return
	}
	st.pushdown(node)
	mid := (l + r) >> 1
	if end <= mid {
		st.Add(node.Left, l, mid, start, end, x)
	} else if start > mid {
		st.Add(node.Right, mid+1, r, start, end, x)
	} else {
		st.Add(node.Left, l, mid, start, mid, x)
		st.Add(node.Right, mid+1, r, mid+1, end, x)
	}
	st.pushup(node, mid-l+1, r-mid)
}

func (st *SegmentTree) Query(node *STNode, l, r, start, end int) (res int64) {
	if l == start && r == end {
		return node.Val
	}
	st.pushdown(node)
	mid := (l + r) >> 1
	if end <= mid {
		res = st.Query(node.Left, l, mid, start, end)
	} else if start > mid {
		res = st.Query(node.Right, mid+1, r, start, end)
	} else {
		res = st.Query(node.Left, l, mid, start, mid) &
			st.Query(node.Right, mid+1, r, mid+1, end)
	}
	st.pushup(node, mid-l+1, r-mid)
	return
}

func (st *SegmentTree) pushdown(node *STNode) {
	if node.Left == nil {
		node.Left = new(STNode)
	}
	if node.Right == nil {
		node.Right = new(STNode)
	}
	if node.Add > 0 {
        node.Left.Val = node.Val
        node.Right.Val = node.Val
		node.Left.Add = node.Add
		node.Right.Add = node.Add
		node.Add = 0
	}
}
func (st *SegmentTree) pushup(node *STNode, ln, rn int) {
	node.Val = node.Left.Val & node.Right.Val
}


/**
 * Your RangeModule object will be instantiated and called as such:
 * obj := Constructor();
 * obj.AddRange(left,right);
 * param_2 := obj.QueryRange(left,right);
 * obj.RemoveRange(left,right);
 */