# in interviews, can use list/array as stack

# stack implementation using linked list
class Node:
  def __init__(self, val):
    self.val = val
    self.next = None

class Stack:
  def __init__(self):
    self.top = None

  def isEmpty(self):
    return not self.top

  def peek(self):
    return self.top.val if self.top else None

  def push(self, val):
    node = Node(val)
    node.next = self.top
    self.top = node

  def pop(self):
    if self.isEmpty():
      raise Exception("Cannot pop from an empty stack")

    val = self.top.val
    self.top = self.top.next
    return val

# tests
stack = Stack()
assert(stack.isEmpty())
stack.push(1)
assert(not stack.isEmpty())
assert(stack.peek() == 1)
stack.push(2)
assert(stack.peek() == 2)
assert(stack.pop() == 2)
assert(stack.peek() == 1)
assert(stack.pop() == 1)
assert(stack.isEmpty())
