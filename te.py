class Tree(object):
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
root = Tree(3)
root.left=Tree(4)
a = root.left
a.left=Tree(1)
a.right=Tree(2)

