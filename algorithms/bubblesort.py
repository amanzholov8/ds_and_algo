def bubblesort(array):
  isSorted = False
  lastUnsorted = len(array) - 1 # minor optimization
  while not isSorted:
    isSorted = True
    for i in range(lastUnsorted):
      if array[i] > array[i+1]:
        array[i], array[i+1] = array[i+1], array[i] #swap
        isSorted = False
    lastUnsorted -= 1



# tests
array = [10, 2, 7, 4, 5]
bubblesort(array)
assert(array == [2, 4, 5, 7, 10])
