from collections import deque
class TreeNode:
    def __init__(self,val,left=None,right=None) -> None:
        self.val=val
        self.right=right
        self.left=left
    

def inorder(root:TreeNode)->list[list[int]]:
    res=[]
    queues=deque()

    queues.append(root)
    while queues:
        n=len(queues)
        level=[]
        for i in range(n):
            node=queues.popleft()
            if node:#if not None
                level.append(node.val)
                queues.append(node.left) #the if not none statement will handle this
                queues.append(node.right)
        if level:
            res.append(level)
    return res

if __name__=="__main__":
    root=TreeNode(1)
    root.left=TreeNode(2)
    root.right=TreeNode(3)
    root.left.left=TreeNode(4)

    ans=inorder(root)
    print(ans)