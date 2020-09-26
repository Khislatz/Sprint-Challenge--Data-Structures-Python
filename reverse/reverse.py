class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head) # node.next_node = self.head

        self.head = node 

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False


    def reverse_list(self, node, prev):
        # check if the list is empty
        if not self.head:
            return        
        # initialize values
        curr_node = node

        # looping until we reach the end of the list 
        while curr_node is not None:
            # store the tail value in the variable nxt
            nxt = curr_node.get_next()
            # reverse the list
            # overwrite the next node with the previous node
            curr_node.set_next(prev)     

            # move to next node      
            prev = curr_node
            curr_node = nxt

        # initialize the new head
        self.head = prev    



        