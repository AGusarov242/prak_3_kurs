class Node:
	"""docstring for Node"""
	def __init__(self, val = None, next = None):
		self.val = val
		self.next = next

class List:
	def __init__(self):
		self.head = None
		self.tail = None
		self.size = 0

	def __str__(self):
		if self.head != None:
			cur = self.head
			out = 'List [\n' +str(cur.val) +'\n'
			while cur.next != None:
				cur = cur.next
				out += str(cur.val) + '\n'
			return out + ']'
		return 'List []'

	def clear(self):
		self.__init__()

	def add(self, elem):
		self.size+=1
		if self.head == None:
			self.tail = self.head = Node(elem, None)
		else:
			self.tail.next = self.tail = Node(elem, None)

	def Del(self, pos):
		if(self.head == None):
			return
		cur = self.head
		count = 0
		if pos == 0:
			self.head = self.head.next
			return
		while cur != None:
			if count == pos:
				if cur.next == None:
					self.tail = cur
				old.next = cur.next
				break
			old = cur
			cur = cur.next
			count += 1

l = List()
l.add(2**100000)
l.add(2)
print(l)

