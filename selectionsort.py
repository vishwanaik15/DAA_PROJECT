#selectionsort
import time 
from time import sleep
def selectionSort(nlist):
  start_time=time.time()
  for fillslot in range(len(nlist)-1,0,-1):
      positionOfMax=0
      for location in range(1,fillslot+1):
          if nlist[location]>nlist[positionOfMax]:
             positionOfMax = location

      temp = nlist[fillslot]
      nlist[fillslot] = nlist[positionOfMax]
      nlist[positionOfMax] = temp
  selection_sort_time =time.time() - start_time
  return nlist,selection_sort_time 
