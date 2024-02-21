class BinarySearchTree:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.tree = None

    def insert(self, data):
        if self.tree is None:
            self.tree = self.Node(data)
        else:
            self._insert(data, self.tree)

    """
    将数据插入到给定节点为根的二叉搜索树中。
    :param data: 要插入的数据
    :param node: 二叉搜索树的根节点
    :return: 无
    """
    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = self.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = self.Node(data)
            else:
                self._insert(data, node.right)

    def find(self, data):
        if self.tree is None:
            return None
        else:
            return self._find(data, self.tree)

    def _find(self, data, node):
        if data == node.data:
            return node
        elif data < node.data:
            if node.left is None:
                return None
            else:
                return self._find(data, node.left)
        else:
            if node.right is None:
                return None
            else:
                return self._find(data, node.right)

    def delete(self, data):
        if self.tree is None:
            return
        else:
            self._delete(data, self.tree)


def test_binary_search_tree():
    binary_search_tree = BinarySearchTree()
    data = [1, 10, 20, 40, 13]
    for i in data:
        binary_search_tree.insert(i)
        assert 20 == binary_search_tree.find(20).data
        binary_search_tree.delete(20)
        assert binary_search_tree.find(20) is None
        # 1 10 40 13
        binary_search_tree.pre_order(binary_search_tree.tree)
        print("--------------------------")
        # 1 10 13 40
        binary_search_tree.in_order(binary_search_tree.tree)
        print("--------------------------")
        # 13 40 10 1
        binary_search_tree.post_order(binary_search_tree.tree)
        print("--------------------------")

if __name__ == '__main__':
    test_binary_search_tree()
