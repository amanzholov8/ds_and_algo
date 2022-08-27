# simple, but creates arrays:
def quicksort(array):
  if len(array) < 2:
    return array
  pivot = array[0]
  less = [i for i in array[1:] if i <= pivot]
  greater = [i for i in array[1:] if i > pivot]
  return quicksort(less) + [pivot] + quicksort(greater)


# in place:
def quicksort_inplace(array):
  def sort(left, right):
    if left >= right:
      return
    pivot = array[(left + right) // 2]
    ind = partition(left, right, pivot)
    sort(left, ind - 1)
    sort(ind, right)

  def partition(left, right, pivot):
    while left <= right:
      while array[left] < pivot:
        left += 1
      while array[right] > pivot:
        right -= 1
      if left <= right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1
    return left

  sort(0, len(array) - 1)


# test:
print(quicksort([10, 5, 2, 3]))

array = [10, 5, 2, 3]
quicksort_inplace(array)
print(array)
