class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

class LinkedList:
	def __init__(self, arr):
		self.arr = arr
		self.head = None
		for i in arr:
			self.insertAtEnd(i)

	def print(self):
		curr = self.head
		while curr:
			print(curr.data, end = " ")
			curr = curr.next

	def insertAtEnd(self, data):
		if self.head == None:
			self.head = Node(data)
		else:
			curr = self.head
			while curr.next:
				curr = curr.next
			curr.next = Node(data)

	def insertAtBeg(self, data):
		temp = Node(data)
		temp.next = self.head
		self.head = temp

	def insertAtPos(self, data, pos):
		if pos == 1:
			self.insertAtBeg(data)
			return 
		count = 0
		curr = self.head
		while curr:
			count += 1
			curr = curr.next
		if count+1<pos:
			return "Can't insert at position"
		else:
			temp = Node(data)
			curr = self.head
			for i in range(pos - 2):
				curr = curr.next
			temp.next = curr.next
			curr.next = temp
		return self.head

if __name__ == "__main__":
	arr = [1, 2, 3, 4, 5]
	l = LinkedList(arr)
	l.print()
	print()
	
	l.insertAtBeg(0)
	l.print()
	print()
	
	l.insertAtEnd(6)
	l.print()
	print()

	l.insertAtPos(2, 2)
	l.print()
	print()