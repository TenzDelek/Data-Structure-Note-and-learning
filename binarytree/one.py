class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val=val
        self.left=left
        self.right=right

def dfs(root):
    if root is None:  # Check if the tree is empty
        return
    stack1=[root]
    while(len(stack1)>0):
        current=stack1.pop()
        print(current.val)
        
        if(current.right):
            stack1.append(current.right)
        if(current.left):
            stack1.append(current.left)
a=TreeNode('a')
b=TreeNode('b')
c=TreeNode('c') 
d=TreeNode('d')
e=TreeNode('e')

a.left=b
a.right=c
b.right=d
b.left=e
'''
        a
       / \
      b   c
     / \
    e   d

    abedc
'''
dfs(a)