class BinarySearchTree:
    class Node:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = self.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, root):
        if data < root.value:
            if root.left is None:
                root.left = self.Node(data)
            else:
                self._insert(data, root.left)
        else:
            if root.right is None:
                root.right = self.Node(data)
            else:
                self._insert(data, root.right)

    def find(self, data):
        if self.root is None:
            return None
        else:
            return self._find(data, self.root)

    def _find(self, data, root):
        if data == root.value:
            return root
        elif data < root.value:
            if root.left is None:
                return None
            else:
                return self._find(data, root.left)
        else:
            if root.right is None:
                return None
            else:
                return self._find(data, root.right)

    def delete(self, data):
        if self.root is None:
            return None
        else:
            parent = None
            self._delete(data, parent, self.root)

    def _delete(self, data, parent, current):
        self.current = self.root
        if current is None:
            return None
        if data < current.value:
            parent = current
            self._delete(data, parent, current.left)
        elif data > current.value:
            parent = current
            self._delete(data, parent, current.right)
        # 要删除的值等于当前节点的值
        else:
            # 当前节点没有子节点
            if current.left is None and current.right is None:
                # 如果是根节点
                if parent is None:
                    self.root = None
                # 如果不是根节点
                elif parent.left == current:
                    parent.left = None
                else:
                    parent.right = None
                return None
            # 当前节点有一个子节点
            elif current.left is None and current.right is not None:
                if parent is None:
                    self.root = current.right
                else:
                    if parent.left == current:
                        parent.left = current.right
                    else:
                        parent.right = current.right
            elif current.left is not None and current.right is None:
                if parent is None:
                    self.root = current.left
                else:
                    if parent.left == current:
                        parent.left = current.left
                    else:
                        parent.right = current.left
            # 当前节点有两个子节点
            else:
                parent = current
                min_node = self._find_min(current.right)
                current.value = min_node.value
                self._delete(min_node.value, parent, current.right)
            return current

        '''
        else:
            if root.left is not None and root.right is not None:
                print("左右子树均不为空")
                min_node = self._find_min(root.right)
                root.data = min_node.value

                root.right = self._delete(min_node.value, root.right)
            else:
                if root.left is not None:
                    temp = root.right
                    print(f"左子树不为空,temp={temp}")
                elif root.right is not None:
                    temp = root.left
                    print(f"右子树不为空,temp={temp}")
                else:
                    temp = None
                    print(f"左右子树均为空,temp={temp}")
                root = temp
            return root
        '''

    def _find_min(self, root):
        while root.left is not None:
            root = root.left
        return root
        '''
        if node.left is None:
            return node
        else:
            return self._find_min(node.left)
        '''

    def pre_order(self, node):
        if node is None:
            return
        print(node.value)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def in_order(self, node):
        if node is None:
            return
        self.in_order(node.left)
        print(node.value)
        self.in_order(node.right)

    def post_order(self, node):
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.value)


def test_binary_search_tree():
    binary_search_tree = BinarySearchTree()
    value = [1, 10, 20, 40, 13, 50]
    for i in value:
        binary_search_tree.insert(i)
    assert 20 == binary_search_tree.find(20).value
    binary_search_tree.delete(20)
    # assert binary_search_tree.find(13) is None
    print("--------------------------")
    # 1 10 40 13
    binary_search_tree.pre_order(binary_search_tree.root)
    print("--------------------------")
    # 1 10 13 40
    binary_search_tree.in_order(binary_search_tree.root)
    print("--------------------------")
    # 13 40 10 1
    binary_search_tree.post_order(binary_search_tree.root)
    print("--------------------------")


if __name__ == '__main__':
    test_binary_search_tree()
