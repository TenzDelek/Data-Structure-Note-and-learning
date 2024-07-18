# trick (look as a eye of subtree)
- look at the sub tree and apply the traversal 
              1
        2           3
    4        5    6      7
          8
here the inorder(left,root,right)
deep step analysis:
1. first it will go to 1 
2. then rule is Left first so left is 2
3. now when we reach 2 there is subtree so again rule(left is 4)
4. 4 has no left so it is printed  arr=4
5. now next rule is root so arr=4,2
6. but the right has a subtree so rule: 5 left is 8 so arr=4,2,8
7. so 8 root is 5 and so arr=4,2,8,5
8. now everything is done the left root and right for the whole left subtree(from root view)
9. now root get in as Left is done now root so arr=4,2,8,5,1
10. and so on arr=4,2,8,5,1,6,3,7