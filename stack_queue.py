class Queue:
	def __init__ (self):
		self.data = []

	def push(self,item):
		self.data.append(item)

	def pop(self):
		return self.data.pop(0)

	def isEmpty(self):
		if len(self.data) == 0:	
			return True
		else:
			return False

class Stack:
	def __init__ (self):
		self.data = []

	def push(self,item):
		self.data.append(item)

	def pop(self):
		return self.data.pop()

	def isEmpty(self):
		if len(self.data) == 0:	
			return True
		else:
			return False


a = Queue()
a.push(4)
a.pop()
print a.isEmpty()