"""Pure Python."""


class Node(object):
    """Node."""

    def __init__(self, key, parent=None, left=None, right=None):
        """Constructor."""
        self.key = key
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        """String Representation of Node."""
        return "Key:{}\tLeft:{}\tRight:{}\tParent:{}"\
               .format(self.key, self.left, self.right,
                       self.parent.key if self.parent is not None else None)


class BinarySearchTree(object):
    """Binary Search Tree."""

    def __init__(self):
        """Constructor."""
        self.root = None

    def insert(self, value):
        """Insert."""
        if self.root is not None:
            self.__insert_helper(self.root, value)
        else:
            self.root = Node(value, None, None, None)

    def __insert_helper(self, cur_node, value):
        """Insert Helper."""
        if(value < cur_node.key):
            if cur_node.left is None:
                cur_node.left = Node(value)
                cur_node.left.parent = cur_node
            else:
                self.__insert_helper(cur_node.left, value)
        else:
            if cur_node.right is None:
                cur_node.right = Node(value, cur_node)
                cur_node.right.parent = cur_node
            else:
                self.__insert_helper(cur_node.right, value)

    def print(self):
        """Print the BST."""
        self.__inorder_walk(self.root)

    def __inorder_walk(self, cur_node):
        """Inorder walk."""
        if cur_node is not None:
            self.__inorder_walk(cur_node.left)
            print(cur_node.key)
            self.__inorder_walk(cur_node.right)

    def preorder_walk(self, cur_node):
        """Preorder walk."""
        if cur_node is not None:
            print(cur_node.key)
            self.__inorder_walk(cur_node.left)
            self.__inorder_walk(cur_node.right)

    def search(self, value):
        """Search."""
        return BinarySearchTree.__search_helper(self.root, value)

    def __search_helper(cur_node, value):
        """Search Helper."""
        if cur_node is not None:
            if cur_node.key == value:
                return cur_node
            elif value < cur_node.key:
                return BinarySearchTree.__search_helper(cur_node.left, value)
            else:
                return BinarySearchTree.__search_helper(cur_node.right, value)
        else:
            return None

    def __tree_minimum(cur_node):
        """Minimum tree."""
        if cur_node.left is not None:
            return BinarySearchTree.__tree_minimum(cur_node.left)
        else:
            return cur_node

    def __tree_maximum(cur_node):
        """Maximum from the subtree."""
        if cur_node.right is not None:
            return BinarySearchTree.__tree_maximum(cur_node.right)
        else:
            return cur_node

    def successor(self, value):
        """Successor of BST."""
        cur_node = self.search(value)
        if cur_node is not None:
            if cur_node.right is not None:
                return BinarySearchTree.__tree_minimum(cur_node.right)
            else:
                par_node = cur_node.parent
                while par_node is not None and cur_node == par_node.right:
                    cur_node = par_node
                    par_node = cur_node.parent
                return par_node
        else:
            print("Node not found")

    def predecessor(self, value):
        """Predecessor of BST."""
        cur_node = self.search(value)
        if cur_node is not None:
            if cur_node.left is not None:
                return BinarySearchTree.__tree_maximum(cur_node.left)
            else:
                par_node = cur_node.parent
                while par_node is not None and cur_node == par_node.left:
                    cur_node = par_node
                    par_node = cur_node.parent
                return par_node
        else:
            print("Node not found")

    def __has_no_right_child(cur_node):
        return cur_node.right is None

    def __has_no_left_child(cur_node):
        return cur_node.left is None

    def delete(self, value):
        """Delete."""
        cur_node = self.search(value)
        if cur_node is not None:
            if BinarySearchTree.__has_no_left_child(cur_node):
                self.transplant(cur_node, cur_node.right)
            elif BinarySearchTree.__has_no_right_child(cur_node):
                self.transplant(cur_node, cur_node.left)
            else:
                succ_node = BinarySearchTree.__tree_minimum(cur_node.right)
                if succ_node.parent is not cur_node:
                    self.transplant(succ_node, succ_node.right)
                    succ_node.right = cur_node.right
                    succ_node.right.parent = succ_node
                self.transplant(cur_node, succ_node)
                succ_node.left = cur_node.left
                succ_node.left.parent = succ_node
        else:
            print("Node to be deleted is not found in the tree")

    def transplant(self, source, dest):
        """Transplant dest into source."""
        if source.parent is None:
            self.root = dest
        elif source.parent.left == source:
            source.parent.left = dest
        else:
            source.parent.right = dest
        if dest is not None:
            dest.parent = source.parent


def choose_bst_option(option, bst):
    """Choose an option in bst."""
    if option == 0:
        bst.print()
    elif option == 1:
        node_val = input("Enter the value to be inserted")
        bst.insert(int(node_val))
        bst.print()
    elif option == 2:
        node_val = input("Enter the value to be deleted")
        bst.delete(int(node_val))
        bst.print()
    elif option == 3:
        node_val = input("Enter the value to be searched")
        print(bst.search(int(node_val)))
    elif option == 4:
        node_val = input("Enter the value to find the predecessor")
        print(bst.predecessor(int(node_val)))
    elif option == 5:
        node_val = input("Enter the value to find the successor")
        print(bst.successor(int(node_val)))
    elif option == 6:
        bst.preorder_walk()
    else:
        print("Invalid Option")

if __name__ == '__main__':
    bst = BinarySearchTree()
    while True:
        print("Choose an BST option")
        node_value = input("0.Print,1.Insert,2.Delete,3.Search,4.Predecessor,\
5.Successor,6.Preorder\n")
        try:
            node_value = int(node_value)
            choose_bst_option(node_value, bst)
        except ValueError:
            print("You entered an invalid number")
