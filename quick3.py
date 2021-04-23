#quick3
import time
from time import sleep

def find_pivot(nlist,low,high):
    mid = (low+high)//2
    if nlist[low]<=nlist[mid]:
        if nlist[mid]<=nlist[high]:
            pivot = nlist[mid]
            temp = nlist[mid]
            nlist[mid] = nlist[high]
            nlist[high] = temp
        elif nlist[mid] > nlist[high]:
            if nlist[high] > nlist[low]:
                pivot = nlist[high]
            else:
                pivot = nlist[low]
                temp = nlist[low]
                nlist[low] = nlist[high]
                nlist[high] = temp
    else:
        if nlist[mid] > nlist[high]:
            pivot = nlist[mid]
            temp = nlist[mid]
            nlist[mid] = nlist[low]
            nlist[low] = nlist[high]
            nlist[high] = temp
        elif nlist[high] > nlist[mid]:
            if nlist[high] <= nlist[low]:        
                pivot = nlist[high]
                temp = nlist[low]
                nlist[low] = nlist[mid]
                nlist[mid] = temp
            else:
                pivot = nlist[low]
                temp = nlist[high]
                nlist[high] = nlist[low]
                nlist[low] = nlist[mid]
                nlist[mid] = temp
    return pivot

def partition(nlist,low,high):
    pivot = find_pivot(nlist,low,high)
    first = low-1
    for i in range(low,high):
        if nlist[i]<=pivot:
            first = first + 1
            temp = nlist[first]
            nlist[first] = nlist[i]
            nlist[i] = temp
    temp = nlist[first+1]
    nlist[first+1] = nlist[high]
    nlist[high] = temp	
    return first+1

def quicksortmed(nlist,low,high):
    start_time = time.time()
    if low<high:
        length = partition(nlist,low,high)
        quicksortmed(nlist,low,length-1)
        quicksortmed(nlist,length+1,high)
    quick_sort_time = time.time() - start_time
    return nlist,quick_sort_time


