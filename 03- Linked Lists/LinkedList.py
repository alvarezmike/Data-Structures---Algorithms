class Node:
    def __init__(self, value):
        """Node constructor """
        self.value = value
        self.next = None

class LinkedLists:
    def __init__(self, value):
        """Linked List constructor """
        new_node = Node(value)
        self.head =  new_node
        self.tail = new_node
        self.length = 1


    def print_list(self):
        """Method to print all values of a list"""
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp =temp.next

    def append(self, value):
        """Method to append to the end of the Linked list"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True




my_linked_list = LinkedLists(1)
my_linked_list.append(2)
my_linked_list.print_list()