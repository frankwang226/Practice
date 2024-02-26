'''
实现一个算法，确定一个字符串 s 的所有字符是否全都不同。

示例 1：

输入: s = "leetcode"
输出: false
示例 2：

输入: s = "abc"
输出: true
限制：

0 <= len(s) <= 100
s[i]仅包含小写字母
如果你不使用额外的数据结构，会很加分。
'''
class Solution:
    def isUnique(self, astr: str) -> bool:
        list = []
        for i in range(0, len(astr) - 1):
            if astr[i] in astr[i + 1:]:
                list.append(astr[i])
        if not list:
            return True
        else:
            return False

def test_isUnique():
    str = Solution()
    assert False == str.isUnique("leecode")
    assert True == str.isUnique("abc")


if __name__ == '__main__':
    test_isUnique()
