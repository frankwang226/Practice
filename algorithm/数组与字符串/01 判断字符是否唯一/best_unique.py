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
    mark = 0
    for char in astr:
      move_bit = ord(char) - ord('a')
      if (mark & (1 << move_bit)) != 0:
        return False
      else:
        mark |= (1 << move_bit)
    return True

def test_isUnique():
    str = Solution()
    assert False == str.isUnique("leecode")
    assert True == str.isUnique("abc")

if __name__ == '__main__':
    test_isUnique()