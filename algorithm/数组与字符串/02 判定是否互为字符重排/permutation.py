'''
给定两个由小写字母组成的字符串 s1 和 s2，请编写一个程序，确定其中一个字符串的字符重新排列后，能否变成另一个字符串。

示例 1：

输入: s1 = "abc", s2 = "bca"
输出: true
示例 2：

输入: s1 = "abc", s2 = "bad"
输出: false
说明：

0 <= len(s1) <= 100
0 <= len(s2) <= 100
'''


class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        for char in s1:
            if char not in s2:
                return False
            else:
                s2 = s2.replace(char, '', 1)
        if s2 == '':
            return True
        else:
            return False


def test_CheckPermutation():
    permutation = Solution()
    assert True == permutation.CheckPermutation("abc", "bca")
    assert False == permutation.CheckPermutation("abc", "bad")
    assert False == permutation.CheckPermutation("abb", "aab")


if __name__ == '__main__':
    test_CheckPermutation()
