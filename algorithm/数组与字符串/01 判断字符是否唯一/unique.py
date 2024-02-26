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
