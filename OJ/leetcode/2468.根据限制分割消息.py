# 题目：2468.根据限制分割消息
# 难度：HARD
# 最后提交：2022-11-13 14:35:48 +0800 CST
# 语言：python3
# 作者：ZrjaK

class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        # note - 1 表示对应位数 v 的最长可能结果列表长度，用 v 来进行枚举
        note, v = 1, 0
        while True:
            note *= 10
            v += 1
            # 最终需要填下 f'<10..0/99..9>'，limit 应至少大于其位数，否则不存在分割结果
            if 2 * v + 3 > limit: return []
            # length 描述对应标号的位数的大小，而 cnt 表示积累的总可填写字符串位置的数量
            # 可以填字符的位置为 limit - length(分子) - 3('</>') - v(分母) 个，位数为 length 的数字共有 9 * pow(10, length - 1) 个
            cnt = sum((limit - length - 3 - v) * 9 * pow(10, length - 1) for length in range(1, v+1))
            if cnt >= len(message): break
        ans = []
        for char in message:
            # 在前字符串填满的情况下加入新字符串
            if len(ans) == 0 or len(ans[-1]) + len(str(len(ans))) + 3 + v == limit: ans.append('')
            ans[-1] += char
        # 输出的过程中，补充前面没有加入字符串的 '</>' 部分
        return [x + f'<{idx}/{len(ans)}>' for idx, x in enumerate(ans, 1)]