# Binary Tree Implementation

from collections import deque

class Node:
 def __init__(self, data):
	self.data = data
	self.left = None
	self.right = None

queue = deque()
def insert(root, val):
	newNode = Node(val)
	if not root:
		return newNode
	queue.append(root)
	while queue:
		node = queue.popleft()
		if not node.left:
			node.left = newNode
			break
		else:
			queue.append(node.left)
		if not node.right:
			node.right = newNode
			break
		else:
			queue.append(node.right)
	return root

def inorder(root):
	if not root:
		return []
	l = []
	