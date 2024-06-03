# time complexity is big O of N


class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left =left
        self.right= right
    

def nodeatk(root,k):
    if not root:
        return
    if k==0:
        #that means the distance is cover
        print(f'i am the node: {root.val}')
    else:
        nodeatk(root.left,k-1)
        nodeatk(root.right,k-1)

def depth(root):
    if not root:
        return 0
    else:
        left=depth(root.left)
        right=depth(root.right)
        return max(left,right)+1

def inorder(root):
    if not root:
        return
    inorder(root.left)
    print(root.val)
    inorder(root.right)

a=TreeNode("a")
b=TreeNode("b")
c=TreeNode("c")
d=TreeNode("d")
e=TreeNode("e")

a.left=b
a.right=c
a.left.left=d
a.left.right=e
# inorder(a)
'''
    a
    /\
   b  c
  / \ 
 d   e
inorder- dbeac
'''

#depth
print(depth(a))

#node at k distance
nodeatk(a,2)