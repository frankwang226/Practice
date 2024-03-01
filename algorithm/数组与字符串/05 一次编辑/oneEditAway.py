'''
字符串有三种编辑操作:插入一个英文字符、删除一个英文字符或者替换一个英文字符。 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。

示例 1:

输入:
first = "pale"
second = "ple"
输出: True

示例 2:

输入:
first = "pales"
second = "pal"
输出: False
'''


class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        lf, ls = len(first), len(second)
        if lf > ls:
            return self.oneEditAway(second, first)
        if ls - lf > 1:
            return False
        if ls == lf:
            diff = 0
            for i in range(lf):
                if first[i] != second[i]:
                    diff += 1
            if diff > 1:
                return False
            else:
                return True
        else:
            ofs = 0
            for i in range(lf):
                while first[i] != second[i+ofs]:
                    ofs += 1
                    if ofs > 1:
                        return False
            if ofs > 1:
                return False
            else:
                return True

    def best_oneEditAway(self, first: str, second: str) -> bool:
        lf, ls = len(first), len(second)
        if lf > ls:
            return self.oneEditAway(second, first)
        if ls - lf > 1:
            return False
        if lf == ls:
            count = 0
            for i in range(lf):
                if first[i] != second[i]:
                    count += 1
            return count <= 1
        i, ofs = 0, 0
        while i < lf:
            if first[i] != second[i + ofs]:
                ofs += 1
                if ofs > 1:
                    return False
            else:
                i += 1
        return True


    def test_oneEditAway(self):
        result = Solution()
        assert False == result.oneEditAway("horse", "ros")
        assert False == result.oneEditAway("pales", "pal")
        assert True == result.oneEditAway("pale", "bale")
        assert False == result.oneEditAway("pale", "bae")
        assert False == result.oneEditAway("pale", "bake")
        assert True == result.oneEditAway("pale", "pale")
        assert True == result.oneEditAway("pale", "bale")
        assert False == result.oneEditAway("orsq", "horse")

        assert False == result.best_oneEditAway("horse", "ros")
        assert False == result.best_oneEditAway("pales", "pal")
        assert True == result.best_oneEditAway("pale", "bale")
        assert False == result.best_oneEditAway("pale", "bae")
        assert False == result.best_oneEditAway("pale", "bake")
        assert True == result.best_oneEditAway("pale", "pale")
        assert True == result.best_oneEditAway("pale", "bale")
        assert False == result.best_oneEditAway("orsq", "horse")


if __name__ == '__main__':
    test = Solution()
    test.test_oneEditAway()
