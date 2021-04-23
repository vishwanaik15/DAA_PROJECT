#bubblesort
import time 
from time import sleep
def bubbleSort(nlist):
  start_time=time.time()
  for passnum in range(len(nlist)-1,0,-1):
      for i in range(passnum):
          if nlist[i]>nlist[i+1]:
              temp = nlist[i]
              nlist[i] = nlist[i+1]
              nlist[i+1] = temp
  bubble_sort_time =time.time() - start_time
  return nlist,bubble_sort_time






  