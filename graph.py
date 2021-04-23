import time
import random as rng
import sys 
import matplotlib.pyplot as plt 
from insertionsort import insertionSort
from heapsort import heapSort,heapify
from bubblesort import bubbleSort
from mergesort import MergeSort
x=int(input('Enter number of iterations :'))
n=20
bt=[]
mt=[]
ht=[]
it=[]
qt=[]
number=[]
for i in range(x):
        

        bubbleinput=[]
        mergeinput=[]
        heapinput=[]
        insertinput=[]
        
        for j in range(0,n):
                a=rng.randint(-n,n)
                bubbleinput.append(a)
                mergeinput.append(a)
                heapinput.append(a)
                insertinput.append(a)
                quickinput.append(a)

        bubbletime=bubbleSort(bubbleinput)
        mergetime=MergeSort(mergeinput)
        heaptime=heapSort(heapinput)
        inserttime=insertionSort(insertinput)
        mt.append(mergetime)
        ht.append(heaptime)
        it.append(inserttime)
        number.append(n)
        n=n*2
print(number)
plt.plot(number,bt, label = "Bubble Sort")
plt.plot(number,mt, label = "Merge Sort")
plt.plot(number,ht, label = "Heap Sort")
plt.plot(number,it, label = "Insertion Sort")
plt.xlabel('input size')  
plt.ylabel('time')
plt.title('Comparison !!')
plt.legend() 
plt.show()




