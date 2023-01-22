class Node(object):
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(object):
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        if self.root is None:
            self.root = Node(value)
            return

        def _insert(node: Node, value: int) -> Node:
            if node is None:
                return Node(value)

            if value < node.value:
                node.left = _insert(node.left, value)
            else:
                node.right = _insert(node.right, value)
            return node

        _insert(self.root, value)

    def in_order(self) -> None:
        def _in_order(node: Node) -> None:
            if node is not None:
                _in_order(node.left)
                print(node.value, end=" ")
                _in_order(node.right)

        _in_order(self.root)

    def search(self, value: int) -> bool:
        def _search(node: Node, value: int) -> bool:
            if node is None:
                return False

            if value == node.value:
                return True
            elif value > node.value:
                return _search(node.right, value)
            else:
                return _search(node.left, value)

        return _search(self.root, value)

    def min_value(self, node: Node) -> Node:
        current = node
        while current.left is not None:
            current = current.left
        return current

    def remove(self, value: int) -> Node:
        def _remove(node: Node, value: int) -> Node:
            if node is None:
                return node
            if value < node.value:
                node.left = _remove(node.left, value)
            elif value > node.value:
                node.right = _remove(node.right, value)
            else:
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left

                # You don't have to check the left
                # because the value of the node should be larger.
                tmp = self.min_value(node.right)
                node.value = tmp.value
                node.right = _remove(node.right, tmp.value)
            return node

        _remove(self.root, value)


if __name__ == "__main__":
    binary_tree = BinarySearchTree()
    binary_tree.insert(3)
    binary_tree.insert(1)
    binary_tree.insert(6)
    binary_tree.insert(2)
    binary_tree.insert(5)
    binary_tree.insert(7)
    binary_tree.insert(10)
    binary_tree.in_order()
    print()

    assert binary_tree.search(7)

    binary_tree.remove(3)
    binary_tree.remove(7)
    binary_tree.in_order()
    print()

    assert not binary_tree.search(7)
