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