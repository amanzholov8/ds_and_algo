# queue implementation using linked list
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Queue:
  def __init__(self):
    self.head = None # remove from the head
    self.tail = None # add to the tail

  def isEmpty(self):
    return self.head == None

  def peek(self):
    return self.head.val if self.head else None

  def enqueue(self, val):
    node = Node(val)
    if self.tail:
      self.tail.next = node
    self.tail = node
    if not self.head:
      self.head = node

  def dequeue(self):
    if self.isEmpty():
      raise Exception("Cannot dequeue an empty queue")

    val = self.head.val
    self.head = self.head.next
    if not self.head:
      self.tail = None
    return val

# tests
queue = Queue()
assert(queue.isEmpty())
queue.enqueue(10)
assert(not queue.isEmpty())
assert(queue.peek() == 10)
queue.enqueue(12)
assert(queue.peek() == 10)
assert(queue.dequeue() == 10)
assert(queue.peek() == 12)
assert(queue.dequeue() == 12)
assert(queue.isEmpty())
