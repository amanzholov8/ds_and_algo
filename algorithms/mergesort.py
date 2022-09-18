def mergesort(array):
  if len(array) <= 1:
    return array
  mid = len(array) // 2
  leftHalf = mergesort(array[:mid])
  rightHalf = mergesort(array[mid:])
  return merge(leftHalf, rightHalf)

def merge(array1, array2):
  res = []
  i, j = 0, 0
  while i < len(array1) and j < len(array2):
    if array1[i] < array2[j]:
      res.append(array1[i])
      i += 1
    else:
      res.append(array2[j])
      j += 1

  res += array1[i:]
  res += array2[j:]
  return res

# tests
array = [10, 2, 7, 4, 5]
assert(mergesort(array) == [2, 4, 5, 7, 10])
