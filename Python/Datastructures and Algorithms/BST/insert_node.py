class Node:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None




def insert(root, key):
    
    if root is None:
        return(Node(key))
        
    if root.key == key :
        return root
    if root.key > key :
            
        root.left = insert(root.left, key)
        
    else :
        root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.key, end=" ")
        inorder(root.right)

root = Node(80)

root = insert(root, 40)
root = insert(root, 90)
root = insert(root, 20)
root = insert(root, 60)
inorder(root)
