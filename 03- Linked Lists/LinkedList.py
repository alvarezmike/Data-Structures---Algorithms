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

    def pop(self):
        """Method to remove last item (tail) from list"""
        if self.length ==0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp= temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.lenght == 0:
            self.head = None
            self.tail = None
        return temp.value

    def prepend(self, value):
        """ Method to add a new node to beginning of list (head)"""
        new_node = Node(value)
        if self.lenght == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def popfirst(self):
        """Method to remove first item in list (head)"""
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def get(self, index):
        """Method to get node of specified index on list"""
        if index <= 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def set_value(self, index, value):
        """Method to set a value on specified index """
        temp = self.get(index)
        if temp is not None:
            temp.value = value
            return  True
        return False

    def insert(self, index,value):
        """Method to insert a new node at a specified index on the list"""
        if index < 0  or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node (value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        """Method to remove a node from a specific index"""
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.popfirst()
        if index == self.length - 1:
            return self.pop()
        prev = self.get(index -1 )
        temp = prev.next
        prev.next = temp.next
        temp.next = None
        self.length -=1
        return  temp

    def reverse(self):
        """Method to reverse a linked list, convert the tail the head, and the head the tail"""
        temp = self.head
        self.head = self.tail
        self.tail = temp
        after = temp.next
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after



my_linked_list = LinkedLists(1)
my_linked_list.append(2)
my_linked_list.append(5)
my_linked_list.append(8)
my_linked_list.print_list()
print("Now will reverse")

my_linked_list.reverse()

my_linked_list.print_list()