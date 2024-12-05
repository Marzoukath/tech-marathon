class Node:
    
    def __init__(self, key):
        self.key = key
        self.right=None
        self.left=None

def Search(root, key):

    if root is None or root.key == key :
        return root
    if root.key < key:
        return(Search(root.right, key))
    return(Search(root.left, key))

root = Node(10)
root.left= Node(5)
root.right= Node(20)
root.left.left = Node(2)
root.left.right = Node(7)
root.right.left = Node(17)
root.right.right = Node(30)
print(Search(root,20), Search(root, 0))

