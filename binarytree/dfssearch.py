# so the breadth first search works as it is named
# suppose we have a tree
'''
        a
       / \
      b   c
     / \
    e   d

'''
#if the iteration is like a,b,c,e,d then it is bfs
#see first we go from the first level then next then next
#Unlike dfs(where we first go to the whole left and then right)

#implementation
# bfs are mostly used wuth queue. 
#the below code is the traversal part of it.
'''
a quick pseudocode
1. check if the root is there
2.declare a queue having a initial var as the root
3.now while queue is not empty
4.popleft(start) and store it in a var
5.append it in the result for printing purpose
6.now if the left node is there append it in the queue
7.then do it for the right node
'''
from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right

def dfs(root,search):
    if not root:
        return False
    if root.val == search:
        return True
    return dfs(root.left,search) or dfs(root.right,search)
a=TreeNode('a')
b=TreeNode('b')
c=TreeNode('c') 
d=TreeNode('d')
e=TreeNode('e')
a.left=b
a.right=c
b.right=d
b.left=e
searchletter=input("enter the char: ")
ans=dfs(a,searchletter)
print(ans)