class List:
	'''Class that immutate the structure of single-binded list'''

	def __init__(self, val, next = None):
		'''Constructor'''
		self.val = val
		self.next = next
		self.size = 0

	def __str__(self):
		'''Output rechange'''
		tmp = self
		out = 'List [' +str(tmp.val)
		while tmp.next != None:
			tmp = tmp.next
			out += '->' + str(tmp.val)
		return out + ']'

	def add(self, elem):
		tmp = self
		tmp.size += 1
		if tmp.next == None:
			tmp.next = List(elem, None)
		else:
			while tmp.next != None:
				tmp = tmp.next
			tmp.next = List(elem, None)

	def pos_search(self, pos):
		tmp = self
		count = 0
		while tmp != None:
			if (count == pos):
				print('List[' + str(count) + '] :' + str(tmp.val))
			tmp = tmp.next
			count += 1

def Del(list, pos):
	count = 0
	if (pos == 0):
		tmp = list.next
		del list
		return tmp      
	else:
		cur = list
		while cur != None:
				if count == pos:
					old.next = cur.next
					break
				old = cur
				cur = cur.next
				count += 1
		return list

def into_list(num):
	s = str(num)
	i = int(len(s)-2)
	tlist = List(int(s[i+1]), None)
	#tlist.add(int(s[0]))
	while i >= 0:
		tlist.add(int(s[i]))
		i -= 1
	#print(tlist)
	return tlist

def into_num(list):
	num = 0
	while list != None:
		num = 10*num + list.val
		list = list.next
	return num


def Sum(L1,L2):
	n1 = into_num(L1)
	n2 = into_num(L2)
	return into_list(n1 + n2)


l = List(4)
l.add(2)
l.add(2)
l.add(3)
l.pos_search(3)
print(l)
Del(l, 3)
print(l)
print(into_list(124))
print(into_list(111))
print(Sum(into_list(124), into_list(111)))
