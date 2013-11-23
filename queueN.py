class Queue:
	def __init__(self, N):
		self.list = []
		self.limit = N

	def isEmpty(self):
		return self.list == []

	def enqueue(self, item):
		if self.size() < self.limit:
			self.list.append(item)

	def dequeue(self):
		if not self.isEmpty():
			self.list.pop(0)

	def size(self):
		return len(self.list)
