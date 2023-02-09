class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Queue:
    """Queue constructor """
    def __init__(self, value):
        new_node = Node(value)
        self.first= new_node
        self.last = new_node
        self.length = 1

    def print_queue(self):
        """Print items on queue"""
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp= temp.next

    def enqueue(self, value):
        """adding items to the line (queue)"""
        new_node = Node(value)
        if self.first is None:
            self.first = mew_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def dequeue(self):
        """remove item from queue"""
        if self.length == 0:
             return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length += 1
        return temp


# testing methods
my_queue = Queue(5)
my_queue.enqueue(8)
my_queue.enqueue(2)
my_queue.print_queue()

print("after changes")
my_queue.dequeue()

my_queue.print_queue()