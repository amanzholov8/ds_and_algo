#!/usr/bin/python3

class PriorityQueue:
	def __init__(self):
		self.items = []

	def getLeftChildIndex(self, index):
		return index * 2 + 1

	def getRightChildIndex(self, index):
		return index * 2 + 2

	def getParentIndex(self, index):
		return (index - 1) // 2

	def hasLeftChild(self, index):
		return self.getLeftChildIndex(index) < len(self.items)

	def hasRightChild(self, index):
		return self.getRightChildIndex(index) < len(self.items)

	def hasParent(self, index):
		return self.getParentIndex(index) >= 0

	def leftChild(self, index):
		if not self.hasLeftChild(index):
			raise Exception("No left child")
		leftChildIndex = self.getLeftChildIndex(index)
		return self.items[leftChildIndex]

	def rightChild(self, index):
		if not self.hasRightChild(index):
			raise Exception("No right child")
		rightChildIndex = self.getRightChildIndex(index)
		return self.items[rightChildIndex]

	def parent(self, index):
		if not self.hasParent(index):
			raise Exception("No parent")
		parentIndex = self.getParentIndex(index)
		return self.items[parentIndex]

	def swap(self, ind1, ind2):
		if ind1 >= len(self.items) or ind2 >= len(self.items):
			raise Exception("Index out of range")
		self.items[ind1], self.items[ind2] = self.items[ind2], self.items[ind1]


	def peek(self):
		if not self.items:
			raise Exception("Heap is empty")
		return self.items[0]

	def pop(self):
		if not self.items:
			raise Exception("Heap is empty. Cannot pop from empty heap")
	  # [10, 15, 20, 17] -> [17, 15, 20]
		res = self.items[0]
		self.items[0] = self.items[-1]
		self.items.pop()
		# bubble down
		self.bubbleDown()
		# return min item
		return res

	def push(self, item):
		# [10, 15, 20, 17] -> [10, 15, 20, 17, 9]
		self.items.append(item)
		# bubble up
		self.bubbleUp()

	def bubbleDown(self):
		currIndex = 0
		while self.hasLeftChild(currIndex):
			smallerChildIndex = self.getLeftChildIndex(currIndex)
			if self.hasRightChild(currIndex) and self.rightChild(currIndex) < self.leftChild(currIndex):
				smallerChildIndex = self.getRightChildIndex(currIndex)
			if self.items[smallerChildIndex] < self.items[currIndex]:
				self.swap(currIndex, smallerChildIndex)
				currIndex = smallerChildIndex
			else:
				break


	def bubbleUp(self):
		currIndex = len(self.items) - 1
		while self.hasParent(currIndex) and self.parent(currIndex) > self.items[currIndex]:
			parentIndex = self.getParentIndex(currIndex)
			self.swap(currIndex, parentIndex)
			currIndex = parentIndex
