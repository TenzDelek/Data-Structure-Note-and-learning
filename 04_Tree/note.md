# Tree Node
> striver

```js
    5
1       6
            3
```
keyword:
1. root : 5 is root
2. children : 5 children are 1 and 6
3. leaf node : 3 and 1 are leaf
4. sub tree : 6 sub tree is 3
5. ancestor : 3 ancestor are 6 and 5

- type of binary tree
1. full bt : either has 0 or 2 child node
2. complete bt: 
all level are filled completed 
                node
         node           node 
      node  node   node     node
- exception:
last level is exception but it should be as left as possible
                 node
         node           node 
      node  node   node    
    - last node one is missing but it allow
    also if u delete that node it is allow
    but if we do like:
                node
         node           node 
      node  node                node    
      where right is fill but left is left out then it is not a complete bt.
      
3. perfect bt: all leaf node are same level
4. balance bt: height of tree is max log(n)
5. Degenerate bt: like a linkedlist
   striaght line
   n=4
            node
        node
    node
node

