class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        
    def insert(self, data=None):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            else:
                self.data = data