'''
1、编写一个递归函数来计算列表包含的元素数。
2、通过递归找到列表中最大的数字。
3、通过递归的方式实现二分查找算法。
'''


class Recursion:
    def count(self, alist):
        count = 0
        if alist == []:
            return count
        else:
            return 1 + self.count(alist[1:])

    def max(self, alist):
        if not alist:
            return
        elif len(alist) == 1:
            return alist[0]
        else:
            return max(alist[0], self.max(alist[1:]))

    def binary_search(self, alist, target):
        if not alist:
            return False
        else:
            mid = len(alist) // 2
            if target == alist[mid]:
                return True
            elif target < alist[mid]:
                return self.binary_search(alist[:mid], target)
            else:
                return self.binary_search(alist[mid + 1:], target)

        pass


if __name__ == '__main__':
    recursion = Recursion()
    print(recursion.count([1, 2, 3, 4, 'dd', 6, 7, 8, 9, 'a', 'b']))
    print(recursion.max([4, 9]))
    print(recursion.binary_search([10, 20, 30, 40, 50, 60, 70, 80, 90], 40))
