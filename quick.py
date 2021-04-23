#quicksort
import time 
from time import sleep
def partition(nlist, low, high):
    
    i = (low -1)
    pivot = nlist[high]
    for j in range(low, high):
        if nlist[j] <= pivot:
            i += 1
            nlist[i], nlist[j] = nlist[j], nlist[i]
    nlist[i+1],nlist[high] = nlist[high], nlist[i+1]
    return (i+1)
            
def quickSort(nlist, low, high):
    start_time=time.time()
    if low < high:
        pi = partition(nlist, low, high)
        quickSort(nlist, low, pi-1)
        quickSort(nlist, pi+1, high)
        quick_sort_time =time.time() - start_time
        return nlist,quick_sort_time

