import time
import os
import random as rnd 
import sys
from time import sleep
import importlib
import matplotlib.pyplot as plt

sys.setrecursionlimit(10000)
print(sys.getrecursionlimit())


choice= int(input("\n You have two options:\n 1: Generate random values  \n 2: Enter your choice of array values \n"))
array=[]

if choice==1:
    print("\nEnter choice for random values: \n 1: Larger random values \n 2: Smaller random values")
    new = int(input())
    if new == 1:
        print("\nEnter length of array you want to generate randomly:")
        length=int(input())
        a = sys.maxsize
        for i in range(length):
            nlist = rnd.randint(-a,a)
            array.append(nlist)
        print("\nRandom array elements are given:")
        print(array)
    elif new == 2:
        print("\nEnter length of array you want to generate randomly:")
        length=int(input())
        for i in range(length):
            nlist = rnd.randint(-length*10,length*10)
            array.append(nlist)
        print("\nGenerated array with your choice of elements:")
        print(array)
    else:
        print("\nPlease enter valid input:\n")
        sys.exit()

elif choice==2:
    print("\nEnter length of array of your choice to generate:")
    length = int(input())
    print("\nEnter the array elements of your choice:")
    for i in range(0,length):
        nlist = int(input())
        array.append(nlist)
    print("\nGenerated array with your choice of elements:")
    print(array)
else:
    print("\nPlease enter valid input:\n")
    sys.exit()

from insertionsort import insertionSort
from heapsort import heapSort,heapify
from selectionsort import selectionSort
from bubblesort import bubbleSort
from mergesort import MergeSort
from quick import quickSort,partition
from quick3 import quicksortmed,partition

print("\nSelect any of the following algorithm to calculate running time:\n")
print(" 0: Insertion Sort \n 1: Selection Sort \n 2: Bubble Sort \n 3: Heap Sort  \n 4: Merge Sort \n 5: Quick Sort \n 6: Quick Sort using 3 medians \n 7: Compare every sorting algorithm's running time \n")
select=int(input())
if select==0:
    print("Your selection: Insertion sort\n")
    ar,time = insertionSort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort by insertion sort: ",time)
elif select==1:
    print("Your selection: Selection sort\n")
    ar,time = selectionSort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort by selection sort: ",time)
elif select==2:
    print("Your selection: Bubble sort\n")
    ar,time = bubbleSort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort by bubble sort: ",time)
elif select==3:
    print("Your selection: Heap sort\n")
    ar,time = heapSort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort by heap sort: ",time)
elif select==4:
    print("Your selection: Merge sort")
    ar,time = MergeSort(array)
    print("\nSorted array: ",ar)
    print("\nTime to sort by merge sort: ",time)
elif select==5:
    print("Your selection: Quick sort")
    ar,time = quickSort(array,0,length-1)
    print("\nSorted array: ",ar)
    print("\nTime to sort by quick sort: ",time)
elif select==6:
    print("Your selection Quick sort using 3 medians")
    ar,time=quicksortmed(array,0,length-1)
    print("\nSorted array: ",ar)
    print("\nTime to sort by quick sort using 3 medians: ",time)
elif select==7: 
    print("Time for all algorithms")
    ar,insertion_time = insertionSort(array)
    ar,selection_time = selectionSort(array)
    ar,bubble_time = bubbleSort(array)
    ar,heap_time = heapSort(array)
    ar,merge_time = MergeSort(array)
    ar,quick_time = quickSort(array,0,length-1)
    ar,quickmed_time = quicksortmed(array,0,length-1)
    print("\nSorted array:",ar)
    print("\nTime required for each algorithm to sort the array:\n")
    print("1. Insertion sort: ",insertion_time)
    print("2. Selection sort: ",selection_time)
    print("3. Bubble sort: ",bubble_time)
    print("4. Heap sort: ",heap_time)
    print("5. Merge sort: ",merge_time)
    print("6. Quick sort: ",quick_time)
    print("7. Quick sort using 3 medians: ",quickmed_time)
    print("\nTotal time required to run all algorithms: ",insertion_time+selection_time+bubble_time+merge_time+quick_time+quickmed_time)
    #let's compare which algorithm requires minimum time

    dict={}
    dict[insertion_time]='Insertion sort'
    dict[selection_time]='Selection sort'
    dict[bubble_time]='Bubble sort'
    dict[heap_time]='Heap sort'
    dict[merge_time]='Merge sort'
    dict[quick_time]='Quick sort'
    dict[quickmed_time]='Quick sort using 3 medians'
    time_list=[]
    time_list.append(insertion_time)
    time_list.append(selection_time)
    time_list.append(bubble_time)
    time_list.append(heap_time)
    time_list.append(merge_time)
    time_list.append(quick_time)
    time_list.append(quickmed_time)
    min_time = min(time_list)
    max_time = max(time_list)
    print("\nFor {} inputs {} runs in MINIMUM time".format(length,dict[min_time]))
    

else:
    print("Invalid choice! Try again...")
    sys.exit()

print("If you want to generate graph then press 1 or press any other key to exit")
graph_input = int(input())
if graph_input != 1:
    sys.exit()
else:
    iter_num = int(input("Enter number of iterations: "))
    length = 3
    input_sizes =[]
    insertion = []
    selection = []
    bubble = []
    heap = []
    array = []
    merge = []
    quick = []
    quickmed = []
    for i in range(iter_num):
        for a in range(length):
            nlist = rnd.randint(-length,length) #generating array for certain different lengths
            array.append(nlist)
        print(array)
        #calculating time for each and everysorting and appending to respective sorting's time list
        ar, insertion_time = insertionSort(array)
        insertion.append(insertion_time)
        ar, selection_time = selectionSort(array)
        selection.append(selection_time)
        ar, bubble_time = bubbleSort(array)
        bubble.append(bubble_time)
        ar, heap_time = insertionSort(array)
        heap.append(heap_time)
        ar, merge_time = MergeSort(array)
        merge.append(merge_time)
        ar,quick_time = quickSort(array,0,len(array)-1)
        quick.append(quick_time)
        ar,quickmed_time = quicksortmed(array,0,len(array)-1)
        quickmed.append(quickmed_time)
        input_sizes.append(length)
        length = length * 3

    print("Input sizes: ",input_sizes)
    plt.plot(input_sizes,insertion,label="Insertion sort")
    plt.plot(input_sizes,selection,label="Selection sort")
    plt.plot(input_sizes,bubble,label="Bubble sort")
    plt.plot(input_sizes,heap,label="Heap sort")
    plt.plot(input_sizes,merge,label="Merge sort")
    plt.plot(input_sizes,quick,label="Quick sort")
    plt.plot(input_sizes,quickmed,label="Quick sort(Using 3 medians)")
    plt.xlabel("Input Size")
    plt.ylabel("Time")
    plt.legend()
    plt.show()
    sys.exit()
