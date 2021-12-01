class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self, root=None):
        self.root = root

    def insert(self, value):
        '''
        Inserts a new root if needed. Runs the insert function.
        '''
        if self.root == None:
            self.root = BST.Node(value)
        else:
            self._insert(value, self.root)
    
    def _insert(self, value, node):
        '''
        Inserts a new value into the BST. If there is no root in the BST, 
        make the value the new root. If the value already exists in the BST,
        do not add the value.
        '''
        if value < node.data:
            if node.left is None:
                node.left = BST.Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.data:
            if node.right is None:
                node.right = BST.Node(value)
            else:
                self._insert(value, node.right)

    def __iter__(self):
        '''
        Traverses forward through BST as iterator
        '''
        yield from self.traverse_forward(self.root)
    
    def traverse_forward(self, node):
        '''
        Traverses forward through BST
        '''
        if node is not None:
            yield from self.traverse_forward(node.left)
            yield node.data
            yield from self.traverse_forward(node.right)

print
bst = BST()
bst.insert(7)
bst.insert(9)
bst.insert(3)
bst.insert(3)
bst.insert(5)
bst.insert(11)
bst.insert(8)

for item in bst:
    print(item) # Expected output: 3 5 7 8 9 11
                # Note that 3 only appears once