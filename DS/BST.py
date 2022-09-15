# binary search tree
class BSTNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def insert(self, val):
    if val == self.val:
      raise Exception("Cannot insert duplicates into binary search tree")
    elif val <= self.val:
      if self.left:
        self.left.insert(val)
      else:
        self.left = BSTNode(val)
    else:
      if self.right:
        self.right.insert(val)
      else:
        self.right = BSTNode(val)

  def contains(self, val):
    if val == self.val:
      return True
    elif val < self.val:
      if not self.left:
        return False
      return self.left.contains(val)
    else:
      if not self.right:
        return False
      return self.right.contains(val)

  def printInOrder(self):
    if self.left:
      self.left.printInOrder()
    print(self.val)
    if self.right:
      self.right.printInOrder()

class BST:
  def __init__(self):
    self.root = None

  def insert(self, val):
    if not self.root:
      self.root = BSTNode(val)
      return
    self.root.insert(val)

  def contains(self, val):
    if not self.root:
      return False
    return self.root.contains(val)

  def printInOrder(self):
    if not self.root:
      print("None")
      return
    self.root.printInOrder()


# tests
bst = BST()
bst.insert(10)
assert(bst.contains(10))
assert(bst.root.val == 10)
bst.insert(12)
assert(bst.contains(12))
bst.insert(8)
assert(bst.contains(8))
bst.insert(11)
assert(bst.contains(11))
bst.insert(9)
assert(bst.contains(9))
bst.printInOrder()