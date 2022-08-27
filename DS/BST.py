class Node:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

class BST: # i.e. binary search tree
  def __init__(self):
    self.root = None

  def insert(self, val):
    if not self.root:
      self.root = Node(val)

    if val <= self.root.val:
      if self.root.left:
        self.root.left.insert(val)
      else:
        self.root.left = Node(val)
    else:
      if self.root.right:
        self.root.right.insert(val)
      else:
        self.root.right = Node(val)

  def contains(self, val):
    if not self.root:
      return False

    if val == self.root.val:
      return True
    elif val < self.roo.val:
      if not self.root.left:
        return False
      return self.root.left.contains(val)
    else:
      if not self.root.right:
        return False
      return self.root.right.contains(val)

  def printInOrder(self):
    if not self.root:
      print("None")
      return
    if self.root.left:
      self.root.left.printInOrder()
    print(self.root.val)
    if self.root.right:
      self.root.right.printInOrder()