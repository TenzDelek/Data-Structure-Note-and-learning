# the question is related with the balanceing the bst. 
''' 
we say it is a balanced if there is only difference of 1
        4
       / \
      1   5
            \
              7
this is count as the depth is only difference of 1

'''
# as per the hint the approach is 
'''
1. first convert to array(inorder)
2. then construct the bst
'''
class TreeNode:
    def __init__(self,val=0,left=None,right=None) -> None:
        self.val=val
        self.left=left
        self.right=right
class Tenzin:
    def balancesearchtree(self,root:TreeNode)->TreeNode:
        arr=[]
        def dfs(node):
            if not node:
                return
            dfs(node.left)
            arr.append(node.val)
            dfs(node.right)
        dfs(root)
        #till here we have traverse and got the sorted arry for bst
        print(arr)
        def baltree(left,right):
            if left>right:
                return None
            mid=(left+right)//2
            node=TreeNode(arr[mid])
            node.left=baltree(left,mid-1)
            node.right=baltree(mid+1,right)
            return node
        return baltree(0,len(arr)-1)

    def tree_to_list(self,root: TreeNode) -> list:
        from collections import deque
        if not root:
            return []
    
        result = []
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node:
                result.append(node.val)
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append(None)
    
    # Trim the trailing None values
    #eq [1, None, 2, None, 3, None, 4, None, None]
    #is trim to [1, None, 2, None, 3, None, 4]
        while result and result[-1] is None:
            result.pop()
    
        return result
if __name__=="__main__":
    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.right.right = TreeNode(4)
    
    

    tenzin = Tenzin()
    balanced_root = tenzin.balancesearchtree(root)

    print("Original BST:")
    print(tenzin.tree_to_list(root))

    tenzin = Tenzin()
    balanced_root = tenzin.balancesearchtree(root)

    print("\nBalanced BST:")
    print(tenzin.tree_to_list(balanced_root))

