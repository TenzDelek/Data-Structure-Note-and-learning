class TreeNode:
    def __init__(self,val=0,left=None,right=None) :
        self.val=val
        self.left=left
        self.right=right

'''
        a
       / \
      b   c
     / \
    e   d

    abedc
'''
def dfs(root):
    if(root==None):
        return []
    leftval=dfs(root.left) #[b,e,d]
    rightval=dfs(root.right) #[c]
    return [root.val,*leftval,*rightval]
a=TreeNode('a')
b=TreeNode('b')
c=TreeNode('c') 
d=TreeNode('d')
e=TreeNode('e')

a.left=b
a.right=c
b.right=d
b.left=e

ans=dfs(a)
print(ans)