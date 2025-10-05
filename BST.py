# BST Implementation (Binary Search Tree)
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None
def insert(root, val):
	if not root:
		return Node(val)
	if val < root.data:
		root.left = insert(root.left, val)
	elif val > root.data:
		root.right = insert(root.right, val)
	return root

def inorder(root):
	if not root:
		return []
	l = []
	l.extend(inorder(root.left))
	l.append(root.data)
	l.extend(inorder(root.right))
	return l
arr = list(map(int, input().split()))
root = None
for i in arr:
	root = insert(root, i)
print(inorder(root))