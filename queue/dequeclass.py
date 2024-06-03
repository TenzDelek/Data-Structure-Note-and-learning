from collections import deque
class Tenzin:
    def __init__(self) -> None:
        self.buffer=deque()
    
    def enqueue(self,val):
        self.buffer.appendleft(val)
    
    def dequeue(self):
        self.buffer.pop()
    
    def addlast(self,val): #not a behavoir(FIFO) of queue but just to see the function i added
        self.buffer.append(val)
    
    def deletefirst(self):  #not a behavoir(FIFO) of queue but just to see the function i added
        self.buffer.popleft()
    
    def sizeofqueue(self):
        return len(self.buffer)
    def isemptyqueue(self):
        return len(self.buffer)==0
    
    
pq=Tenzin()
pq.enqueue("tenzin")
pq.enqueue("delek")
print(pq.buffer)
print(pq.sizeofqueue())
print(pq.isemptyqueue())
pq.addlast("i am added last")
print(pq.buffer)