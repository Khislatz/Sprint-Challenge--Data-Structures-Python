"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 
This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # check if the new nodes value is less than the current nodes value
        if value < self.value:
            # if there is no left child already here
            if self.left is None:
                # add the new node to the left
                # create a BSTNode and encapsulate the value in it then set it to the left
                self.left = BSTNode(value)
            # otherwise call insert on the left node
            else:
                self.left.insert(value)
        # otherwise (the new nodes value is greater than or equal to the current node value)
        else:
            # if there is no right child already here
            if self.right is None:
                # add the new node to the right
                # create a BSTNode and encapsulate the value in it then set it to the right
                self.right = BSTNode(value)
            # otherwise call insert on the right node
            else:
                self.right.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # if the value of the current node matches the target
        if self.value == target:
            # return True
            return True
        # check if the target is less than the current nodes value
        if target < self.value:
            # if there is no left child already here
            if self.left is None:
                # return False
                return False
            # otherwise
            else:
                # return a call of contains on the left child passing in the target value
                return self.left.contains(target)
        # otherwise (the target is greater than the current nodes value)
        else:
            # if there is no right child already here
            if self.right is None:
                # return False
                return False
            # otherwise
            else:
                # return a call of contains on the right child passing in the target value
                return self.right.contains(target)

