'''
the linkedlist is not contigous it can be any where in heap. the next keep track
of the list. usually the header is pointed at the first linkedlist
and now the fisrt linkedlist(m1) head is the start and the next is the m2(next linkedlist
) similarly the next of m2 is m3 and the last linked list point it next to null

'''
class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print (printval.dataval)
         printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon") #giving the first node the head
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2 # Link first Node to second node
e2.nextval = e3 # Link second Node to third node

list.listprint()