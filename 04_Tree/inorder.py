class Node:
    def __init__(self,val):
        self.left=None
        self.right=None
        self.data=val

    
def printtree(root):
    if root is None:
        return

    printtree(root.left)
    print(root.data,end=" ")
    printtree(root.right)

if __name__== "__main__":
    root=Node(7)
    root.left=Node(5)
    root.right=Node(4)
    
    root.left.left=Node(9)
    root.left.right=Node(10)
    
    print("inorder traversal")
    printtree(root)

'''
        7
       / \
      5   4
     / \ / \
    9 10

    op - for in - 9,5,10,7,4
'''