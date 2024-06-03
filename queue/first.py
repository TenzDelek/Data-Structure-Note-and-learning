class Queue:
	def __init__(self, c):
		self.queue = []
		self.front = self.rear = 0
		self.capacity = c
		
	def queueEnqueue(self, data):
		if(self.capacity == self.rear):
			print("\nQueue is full")
		else:
			self.queue.append(data)
			self.rear += 1
			
	def queueDequeue(self):
		if(self.front == self.rear):
			print("Queue is empty")
		else:
			x = self.queue.pop(0)
			self.rear -= 1
			
	def queueDisplay(self):
		if(self.front == self.rear):
			print("\nQueue is Empty")
		for i in self.queue:
			print(i, "<--", end='')
			
	def queueFront(self):
		if(self.front == self.rear):
			print("\nQueue is Empty")

		print("\nFront Element is:",
			self.queue[self.front])

if __name__ == '__main__':
	q = Queue(2)
	q.queueEnqueue(1)
	q.queueFront()
	q.queueEnqueue(2)
	q.queueDequeue()
	q.queueFront()
	
	