from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right

def bfs(root):
    if(not root):
        return 0
    totalsum=0
    que=deque([root])
    while(que):
        cur=que.popleft()
        totalsum+=cur.val
        if(cur.left):
            que.append(cur.left)
        if(cur.right):
            que.append(cur.right)

    return totalsum
a=TreeNode(1)
b=TreeNode(2)
c=TreeNode(3)
d=TreeNode(4)
e=TreeNode(5)

a.left=b
a.right=c
b.left=d
b.right=e

ans=bfs(a)
print(ans)