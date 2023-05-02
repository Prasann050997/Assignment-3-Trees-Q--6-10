# Q-6 Find sum of all left leaves in a given Binary Tree

class Node:
	def __init__(self, k):
		self.data = k
		self.left = None
		self.right = None
		
def sumAllLeftLeaves(node, isleft):
	# base case
	if node is None:
		return 0
		
	if node.left is None and node.right is None and isleft:
		return node.data

	return sumAllLeftLeaves(node.left, True) + sumAllLeftLeaves(node.right, False)

root = Node(20)
root.left = Node(9)
root.right = Node(49)
root.left.right = Node(12)
root.left.left = Node(5)
root.right.left = Node(23)
root.right.right = Node(52)
root.left.right.right = Node(12)
root.right.right.left = Node(50)

print("The sum of leaves is " + str(sumAllLeftLeaves(root, False)))

# Q-7 Find sum of all nodes of the given perfect binary tree

import math

def sumNodes(l):
	
	leafNodeCount = math.pow(2, l - 1);

	sumLastLevel = 0;

	sumLastLevel = ((leafNodeCount *
				(leafNodeCount + 1)) / 2);

	sum = sumLastLevel * l;
	return int(sum);

l = 3;
print (sumNodes(l));

# Q-8 Count subtress that sum up to a given value x in a binary tree

class Node:

	def __init__(self, data):

		self.data = data
		self.left = None
		self.right = None

def getNode(data):

	newNode = Node(data)
	return newNode

count = 0
ptr = None

def countSubtreesWithSumXUtil(root, x):

	global count, ptr

	l = 0
	r = 0

	if (root == None):
		return 0

	l += countSubtreesWithSumXUtil(root.left, x)
	r += countSubtreesWithSumXUtil(root.right, x)

	if (l + r + root.data == x):
		count += 1

	if (ptr != root):
		return l + root.data + r

	return count

if __name__ == '__main__':

	''' binary tree creation
			5
			/ \
		-10 3
		/ \ / \
		9 8 -4 7
	'''
	root = getNode(5)
	root.left = getNode(-10)
	root.right = getNode(3)
	root.left.left = getNode(9)
	root.left.right = getNode(8)
	root.right.left = getNode(-4)
	root.right.right = getNode(7)

	x = 7
	ptr = root

	print("Count = " + str(countSubtreesWithSumXUtil(
		root, x)))

# Q-9 Find maximum level sum in Binary Tree

from collections import deque

class Node:
	
	def __init__(self, key):
		
		self.data = key
		self.left = None
		self.right = None

def maxLevelSum(root):
	
	if (root == None):
		return 0

	result = root.data
	
	q = deque()
	q.append(root)
	
	while (len(q) > 0):
		
		count = len(q)

		sum = 0
		while (count > 0):
			
			temp = q.popleft()

			sum = sum + temp.data
   
			if (temp.left != None):
				q.append(temp.left)
			if (temp.right != None):
				q.append(temp.right)
				
			count -= 1

		result = max(sum, result)

	return result
	
if __name__ == '__main__':
	
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.right = Node(8)
	root.right.right.left = Node(6)
	root.right.right.right = Node(7)

	# Constructed Binary tree is:
	#			 1
	#		 / \
	#		 2	 3
	#	 / \	 \
	#	 4 5	 8
	#				 / \
	#			 6	 7
	print("Maximum level sum is", maxLevelSum(root))

# Q-10 Print the nodes at odd levels of a tree

class newNode:
	def __init__(self, data):
		self.data = data
		self.left = self.right = None

def printOddNodes(root, isOdd = True):
	
	if (root == None):
		return

	if (isOdd):
		print(root.data, end = " ")

	printOddNodes(root.left, not isOdd)
	printOddNodes(root.right, not isOdd)

if __name__ == '__main__':
	root = newNode(1)
	root.left = newNode(2)
	root.right = newNode(3)
	root.left.left = newNode(4)
	root.left.right = newNode(5)
	printOddNodes(root)
	