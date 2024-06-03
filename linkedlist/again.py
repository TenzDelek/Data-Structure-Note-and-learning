#first create node -like define the structure
class Node:
    def __init__(self,val=0,next=None) -> None:
        self.val=val
        self.next=next

# create another class to define the functions
class Solution:
    def reverselinked(self,head:Node):
        prev=None
        cur=head
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        return prev
    def printing(self,head:Node):
        cur=head
        while cur:
            print(cur.val,end="->")
            cur=cur.next
        print("None")
            
#the function here might be the reversing the linked list
#and another function to print it

#then write a object to call it
obj=Solution()

#take input from the user to make a linkedlist
print("input for the array")
length=int(input("enter the size of the linkedlist"))

print("the head and the rest: ")
headval=int(input("enter the value for the head:"))
head=Node(headval)
cur=head
for i in range(length-1):
    valuetoadd=int(input("enter the value: "))
    cur.next=Node(valuetoadd)
    cur=cur.next
#apply function on it and print it
revs=obj.reverselinked(head)
obj.printing(revs)
