class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val=val
        self.left=left
        self.right=right

def dfs(root):
    if root==None:
        return 0
    return root.val + dfs(root.left) +dfs(root.right)

a=TreeNode(1)
b=TreeNode(3)
c=TreeNode(4) 
d=TreeNode(5)
e=TreeNode(6)

a.left=b
a.right=c
b.right=d
b.left=e

ans=dfs(a)
print(ans)