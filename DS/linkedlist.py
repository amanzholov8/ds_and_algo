class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, val):
    if not isinstance(val, int):
      raise TypeError("Value must be an interger")

    if not self.head:
      self.head = Node(val)
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = Node(val)

  def prepend(self, val):
    if not isinstance(val, int):
      raise TypeError("Value must be an interger")

    newHead = Node(val)
    newHead.next = self.head
    self.head = newHead

  def delete(self, val):
    if not isinstance(val, int):
      raise TypeError("Value must be an interger")

    if not self.head:
      raise Exception("Cannot delete from empty linked list")
    if self.head.val == val:
      self.head = self.head.next
      return

    curr = self.head
    while curr.next:
      if curr.next.val == val:
        curr.next = curr.next.next
        return
      curr = curr.next

    raise ValueError(f"linked list does not contain {val}")

# tests
linkedList = LinkedList()
linkedList.append(10)
assert(linkedList.head.val == 10)
linkedList.delete(10)
assert(linkedList.head == None)
linkedList.prepend(9)
assert(linkedList.head.val == 9)
linkedList.append(11)
assert(linkedList.head.next.val == 11)
linkedList.prepend(8)
assert(linkedList.head.val == 8)
linkedList.delete(9)
assert(linkedList.head.next.val == 11)
