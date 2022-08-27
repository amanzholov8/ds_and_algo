class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None

  def append(self, val):
    if not self.head:
      self.head = Node(val)
      return
    curr = self.head
    while curr.next:
      curr = curr.next
    curr.next = Node(val)

  def prepend(self, val):
    newHead = Node(val)
    newHead.next = self.head
    self.head = newHead

  def delete(self, val):
    if not self.head:
      return
    if self.head.val == val:
      self.head = self.head.next

    curr = self.head
    while curr.next:
      if curr.next.val == val:
        curr.next = curr.next.next
        return
      curr = curr.next
