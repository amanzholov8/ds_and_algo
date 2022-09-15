# binary search tree
class BSTNode:
  def __init__(self, val):
    self.val = val
    self.left = None
    self.right = None

  def insert(self, val):
    if val == self.val:
      raise ValueError("Cannot insert duplicates into binary search tree")

    if val <= self.val:
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

  def inOrder(self):
    left = f"{self.left.inOrder()} " if self.left else ""
    right = f" {self.right.inOrder()}" if self.right else ""
    return f"{left}{self.val}{right}"

class BST:
  def __init__(self):
    self.root = None

  def insert(self, val):
    if not isinstance(val, int):
      raise TypeError("Value must be an interger")

    if not self.root:
      self.root = BSTNode(val)
      return
    self.root.insert(val)

  def contains(self, val):
    if not isinstance(val, int):
      raise TypeError("Value must be an interger")

    if not self.root:
      return False
    return self.root.contains(val)

  def printInOrder(self):
    if not self.root:
      print("None")
      return
    print(self.root.inOrder())


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

print(f"print in order: {bst.printInOrder}")
assert(bst.root.inOrder() == "8 9 10 11 12")