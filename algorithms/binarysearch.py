# recursive
def recursive_binarysearch(array, target):
  def helper(l, r):
    if l > r:
      return -1
    mid = (l + r) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      return helper(l, mid - 1)
    return helper(mid + 1, r)

  return helper(0, len(array) - 1)

# iterative
def iterative_binarysearch(array, target):
  l, r = 0, len(array) - 1
  while l <= r:
    mid = (l + r) // 2
    if array[mid] == target:
      return mid
    elif array[mid] > target:
      r = mid - 1
    else:
      l = mid + 1
  return -1

# tests
assert(recursive_binarysearch([1, 2], 1) == 0)
assert(recursive_binarysearch([1, 2, 3], 3) == 2)
assert(recursive_binarysearch([1, 2], 3) == -1)

assert(iterative_binarysearch([1, 2], 1) == 0)
assert(iterative_binarysearch([1, 2, 3], 3) == 2)
assert(iterative_binarysearch([1, 2], 3) == -1)
