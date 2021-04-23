#insertionsort
import time 
from time import sleep
def insertionSort(nlist):
   start_time=time.time()
   for index in range(1,len(nlist)):

     currentvalue = nlist[index]
     position = index

     while position>0 and nlist[position-1]>currentvalue:
         nlist[position]=nlist[position-1]
         position = position-1

     nlist[position]=currentvalue
     insertion_sort_time =time.time() - start_time
     return nlist,insertion_sort_time 


