class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)  # 输入字符串的长度
        max_length = 0  # 最长无重复字串的长度
        start = 0  # 滑动窗口的起始位置
        char_dict = {}  # 字符与其最近出现位置的字典

        for end in range(n):
            if s[end] in char_dict and start <= char_dict[s[end]]:
                # 如果当前字符已经出现过，并且在滑动窗口内，则更新滑动窗口的起始位置
                start = char_dict[s[end]] + 1
            else:
                # 计算当前无重复字串的长度
                max_length = max(max_length, end - start + 1)

            # 更新字符的最近出现位置
            char_dict[s[end]] = end

        return max_length

    def test_lengthOfLongestSubstring(self):
        str = Solution()
        assert 3 == str.lengthOfLongestSubstring("abcbcbca")

if __name__ == '__main__':
    test = Solution()
    test.test_lengthOfLongestSubstring()
