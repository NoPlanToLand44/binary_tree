
# defining the Node class that will serve as the main entity for our binary treee

class Node: 
    def __init__(self, val):
        # we need to have a value and a left and right node, we initialize it only as the root node 
        self.val = val
        self.left = None
        self.right = None
        self.traverse = []
    # make the insert method to insert values according to their value ( left - > right: low - > high )
    def insert(self, val): 
        # if root is None we add to root 
        if self.val is None: 
            self.val = val
        # if the val is < than root we insert to the left
        if val < self.val:
            #check if child exists on the left and add the new node only when we reach the bottom 
            if self.left is None:
                self.left = Node(val)
            else:
                self.left.insert(val)
        elif val > self.val: 
            # check if the right child exists and add the new Node only when we reach the bottom 
            if self.right is None: 
                self.right = Node(val)
            else: 
                self.right.insert(val)
    def inOrder(self, node):
    # base case: 
        if node is None : 
            return []
        # recurse till u find the base 
        self.inOrder(node.left)
        self.traverse.append(node.val)
        self.inOrder(node.right)
        return self.traverse
    
    def preOrder(self, node):
    # base case: 
        if node is None : 
            return []
        # recurse till u find the base
        self.traverse.append(node.val)
        self.preOrder(node.left)
        self.preOrder(node.right)
        return self.traverse

# initialize the class and fill the tree if we run this module directly : 

root = Node(99)
root.insert(5)
root.insert(23)
root.insert(2)
root.insert(1)
root.insert(55)


# make functions to traverse the tree: 
print(root.preOrder(root))
