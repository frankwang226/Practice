'''
给定一个字符串，编写一个函数判定其是否为某个回文串的排列之一。

回文串是指正反两个方向都一样的单词或短语。排列是指字母的重新排列。

回文串不一定是字典当中的单词。


示例1：

输入："tactcoa"
输出：true（排列有"tacocat"、"atcocta"，等等）
'''
from collections import defaultdict


class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        '''
        dic = defaultdict(int)
        for char in s:
            dic[char] += 1
        odd_count = 0
        for value in dic.values():
            if value % 2 == 1:
                odd_count += 1
            if odd_count > 1:
                return False
        return True
        '''
        dic = dict()
        for char in s:
            if char in dic.keys():
                dic[char] += 1
            else:
                dic[char] = 1
        odd_count = 0
        for i in dic:
            if dic[i] % 2 !=0:
                odd_count += 1
            if odd_count > 1:
                return False
        return True

    def test_canPermutePalindrome(self):
        result = Solution()
        assert True == result.canPermutePalindrome("tactcoa")
        assert True == result.canPermutePalindrome("abab")
        assert False == result.canPermutePalindrome("abc")

if __name__ == '__main__':
    test = Solution()
    test.test_canPermutePalindrome()