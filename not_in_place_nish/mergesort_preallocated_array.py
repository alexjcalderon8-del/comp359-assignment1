#this is the type of not in place merge sort where we preallocate a temporary array for the mergesort 

# immplementing - standard mergesort with preallocated memory

import random
import time
from typing import List 
#type hinting to type list

class MergeSortPrealloc:
    
    def sort (self, arr: List[int]) -> List[int]: 
        #method to sort an array
        if len(arr) <= 1:
            return arr
        #if the array is of length 1 or less, it is already sorted
        
        
        temp = [0] * len(arr)  
        #preallocate memory for temporary array
    
        self._mergesort(arr, 0, len(arr) - 1, temp)
        # call mergesort on the entire array, making it recursive
     
    def _mergesort(self, arr: List[int], left: int, right: int, temp: List[int]) -> None:        #method to do mergesort recursively
        if left < right:
            
            mid = (left + right) // 2
            
            #recursively sorting left and right halves
            self._mergesort(arr, left, mid, temp)
            self._mergesort(arr, mid + 1, right, temp)
            
            #merging the sorted halves
            self._merge(arr, left, mid, right, temp)
        pass
        
    
    def _merge(self, arr: List[int], left: int, mid: int, right: int, temp: List[int]) -> None:
        #method to merge two sorted halves
        
        #pointers for left and right halves
        i = left      
        j = mid + 1   
        k = 0         
    
    #merging elements
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp[k] = arr[i]
                i += 1
            else:
                temp[k] = arr[j]
                j += 1
            k += 1
    
    
        while i <= mid:
            temp[k] = arr[i]
            i += 1
            k += 1
    
  
        while j <= right:
            temp[k] = arr[j]
            j += 1
            k += 1
    
    #copying merged elements to original array
        for idx in range(k):
            arr[left + idx] = temp[idx]
        pass
    
    
def test():
    #method to test the implementation or the basic setup        
    sorter = MergeSortPrealloc()
    test_arr = [5, 2, 8, 1, 9, 3] #giving a sample array
    print(f"Original array: {test_arr}")    
    print(f"Sorter class initialized: {sorter}")
        
  
test()