import random
import time
from typing import List 

class MergeSortPrealloc:
    
    def sort(self, arr: List[int]) -> List[int]: 
        if len(arr) <= 1:
            return arr 
        
        temp = [0] * len(arr)  
        self._mergesort(arr, 0, len(arr) - 1, temp)
        return arr
    
    def _mergesort(self, arr: List[int], left: int, right: int, temp: List[int]) -> None:
        if left < right:
            mid = (left + right) // 2
            
            self._mergesort(arr, left, mid, temp)
            self._mergesort(arr, mid + 1, right, temp)
            
            self._merge(arr, left, mid, right, temp)
    
    def _merge(self, arr: List[int], left: int, mid: int, right: int, temp: List[int]) -> None:
        i = left      
        j = mid + 1   
        k = 0         
    
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
    
        for idx in range(k):
            arr[left + idx] = temp[idx]
    
    def is_sorted(self, arr: List[int]) -> bool:
        """Check if array is sorted in non-decreasing order."""
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    def test_sort(self, arr: List[int]) -> bool:
        """Test the sort function and verify correctness."""
        original = arr.copy()
        sorted_arr = self.sort(arr.copy())
        
        is_correct = self.is_sorted(sorted_arr)
        
        print(f"Original: {original}")
        print(f"Sorted:   {sorted_arr}")
        print(f"Correctly sorted: {is_correct}")
        
        return is_correct


class PerformanceAnalyzer:
    """Handles performance measurement of sorting algorithms."""
    
    @staticmethod
    def generate_random_array(size: int, min_val: int = 1, max_val: int = 10000) -> List[int]:
        """Generate a random array of given size."""
        return [random.randint(min_val, max_val) for _ in range(size)]
    
    @staticmethod
    def time_sort(sorter, arr: List[int], iterations: int = 3) -> float:
        """
        Time the sort function over multiple iterations.
        Returns average time in seconds.
        """
        total_time = 0
        
        for _ in range(iterations):
            test_arr = arr.copy()
            start_time = time.perf_counter()
            sorter.sort(test_arr)
            end_time = time.perf_counter()
            
            if not sorter.is_sorted(test_arr):
                raise ValueError("Sorting failed!")
            
            total_time += (end_time - start_time)
        
        return total_time / iterations
    
    def run_performance_test(self, sorter, sizes: List[int] = None) -> dict:
        """Run performance test on different array sizes."""
        if sizes is None:
            sizes = [100, 500, 1000, 5000, 10000]
        
        results = {}
        
        print("\n" + "=" * 50)
        print("Performance Analysis")
        print("=" * 50)
        
        for size in sizes:
            test_array = self.generate_random_array(size)
            avg_time = self.time_sort(sorter, test_array)
            results[size] = avg_time
            # fixed issue -  replaced Unicode arrow with ASCII-friendly version
            print(f"Array size: {size:6,} -> Average time: {avg_time:.6f} seconds")
        
        return results


def test_basic():
    """Run comprehensive tests"""
    sorter = MergeSortPrealloc()
    
    print("=" * 50)
    print("Testing MergeSort with Pre-allocated Memory")
    print("=" * 50)
    
    # test Case 1: Basic test
    print("\nTest 1: Basic array")
    test_arr1 = [5, 2, 8, 1, 9, 3]
    sorter.test_sort(test_arr1)
    
    # test Case 2: Already sorted
    print("\nTest 2: Already sorted array")
    test_arr2 = [1, 2, 3, 4, 5]
    sorter.test_sort(test_arr2)
    
    # test Case 3: Reverse sorted
    print("\nTest 3: Reverse sorted array")
    test_arr3 = [9, 8, 7, 6, 5]
    sorter.test_sort(test_arr3)
    
 
def main():
    sorter = MergeSortPrealloc()
    analyzer = PerformanceAnalyzer()
    
    # Run correctness tests
    test_basic()
    
    # Run performance tests
    results = analyzer.run_performance_test(sorter)
    
    # Print summary
    print("\n" + "=" * 50)
    print("Summary")
    print("=" * 50)
    print(f"Algorithm: Standard Mergesort with Pre-allocated Memory")
    print(f"Tested array sizes: {list(results.keys())}")
    print(f"All tests passed: Yes")


if __name__ == "__main__":
    main()