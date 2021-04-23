# heapsort
import time
from time import sleep
def heapify(nlist, n, i):
   largest = i 
   l = 2 * i + 1 
   r = 2 * i + 2 
   
   if l < n and nlist[i] < nlist[l]:
      largest = l
   
   if r < n and nlist[largest] < nlist[r]:
      largest = r
   
   if largest != i:
      nlist[i],nlist[largest] = nlist[largest],nlist[i] # swap
      # root.
      heapify(nlist, n, largest)
def heapSort(nlist):
  start_time = time.time()
  n = len(nlist)
   
  for i in range(n, -1, -1):
      heapify(nlist, n, i)
   
  for i in range(n-1, 0, -1):
      nlist[i], nlist[0] = nlist[0], nlist[i] # swap
      heapify(nlist, i, 0)
  heap_sort_time =time.time() - start_time
  return nlist,heap_sort_time
