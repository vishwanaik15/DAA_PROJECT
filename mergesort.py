#mergesort
import time 
from time import sleep
def MergeSort(nlist):
    start_time=time.time()
    if len(nlist) >1 :
    
        mid = len(nlist)//2
        left_list = nlist[:mid]
        right_list = nlist[mid:]
        MergeSort(left_list) 
        MergeSort(right_list) 
        i = 0
        j = 0
        k = 0
        while i<len(left_list) and j<len(right_list):
            if left_list[i]< right_list[j]:
                nlist[k] = left_list[i]
                i+=1
                k+=1
            else:
                nlist[k] = right_list[j]
                j+=1
                k+=1
        while i < len(left_list): 
            nlist[k] = left_list[i]
            i+=1
            k+=1

        while j < len(right_list):
            nlist[k] = right_list[j]
            j+=1
            k+=1
    merge_sort_time =time.time() - start_time
    return nlist,merge_sort_time 
          
