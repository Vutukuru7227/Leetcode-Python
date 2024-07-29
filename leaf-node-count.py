class Node:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Tree:

    count = 0

    def __init__(self):
        self.root = None

    def count_leaf_nodes(self, root):
        if root is None:
            return 0
        if root.left is None and root.right is None:
            Tree.count += 1
        queue = [root]
        while len(queue) > 0:
            node = queue.pop(0)

            if node.left is not None:
                self.count_leaf_nodes(node.left)
            else:
                pass

            if node.right is not None:
                self.count_leaf_nodes(node.right)
            else:
                pass
        return Tree.count

def main():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    tree = Tree()
    print(tree.count_leaf_nodes(root))


if __name__ == '__main__':
    main()