
from doubly_linked_list import DoublyLinkedList

class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        # If storage is less than allowed capacity (if there is a space)
        if self.storage.length < self.capacity:
            # add value to tail
            self.storage.add_to_tail(item)
            # if there is only one item in the list, then replace it with the current item
            if self.storage.length == 1:
                self.current = self.storage.head
        # Otherwise
        else:
            # set the current value to the item
            self.current.value = item
            # if the current item is not at the end if the list (at the tail)
            # if we didn't reach the end of the list
            if self.current is not self.storage.tail:
                # set current to the next item
                self.current = self.current.next
            else:
                # otherwise (if we reached the end of the list), replace the head with the new item
                self.current = self.storage.head

    
    def get(self):
        # create an empty buffer list
        print_buffer = []
        # store the head value in the variable node. start with the head  
        node = self.storage.head
        # while we haven't reached the capacity, append a new value
        while node is not None:
            print_buffer.append(node.value)
            node = node.next

        return print_buffer

rb = RingBuffer(5)
rb.append(0)
rb.append(1)
rb.append(2)
rb.append(3)
rb.append(4)
print(rb.get())
rb.append(5)
print(rb.get())
rb.append(6)
print(rb.get())
rb.append(7)
rb.append(8)
print(rb.get())
rb.append(9)
print(rb.get())