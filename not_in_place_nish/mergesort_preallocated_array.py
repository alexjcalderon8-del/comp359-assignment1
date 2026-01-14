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
    
        self.mergesort(arr, 0, len(arr) - 1, temp)
        # call mergesort on the entire array, making it recursive
    
    
    def _mergesort(self, arr: List[int], left: int, right: int, temp: List[int]) -> None:
        #method to do mergesort recursively
        pass
    
    def _merge(self, arr: List[int], left: int, mid: int, right: int, temp: List[int]) -> None:
        #method to merge two sorted halves
        pass
    
    
def test():
    #method to test the implementation or the basic setup        
    sorter = MergeSortPrealloc()
    test_arr = [5, 2, 8, 1, 9, 3] #giving a sample array
    print(f"Original array: {test_arr}")    
    print(f"Sorter class initialized: {sorter}")
        
  
test()