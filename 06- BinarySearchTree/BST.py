class Node:
    def __init__(self, value):
        """Node constructor"""
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        """Binary search tree constructor"""
        self.root = None

    def insert(self, value):
        """Method to insert  a new node into tree"""
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self,value):
        """Verify if the tree contains a specific value"""
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp =  temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

# testing methods
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

print(my_tree.root.value)
print(my_tree.root.left.value)
print(my_tree.root.right.value)
print(my_tree.contains(1))


